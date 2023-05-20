from .models import sales_data_OS, OS_geolocation
from .serializer import OS_SalesSerializer, OS_MonthlySerializer, OSpieSerializer, OS_ReginalManSerializer
from django.http import JsonResponse
import datetime
import json
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
import datetime
from django.db.models.functions import TruncMonth, TruncYear
from django.db.models import Sum
import csv
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage(location='/temp/OS')

# Create your views here.


# ---------------------------------------update-API-------------------------------------------------------


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_db_OS(request):
    data = {}
    if request.user.designation == "Manager":

        try:
            file = request.FILES["file"]
            content = file.read()
            file_content = ContentFile(content)
            file_name = fs.save(file.name, file_content)
            tmp_file = fs.path(file_name)
            csv_file = open(tmp_file, errors="ignore")
            reader = csv.reader(csv_file)
            next(reader)

            product_list = []

            for row in reader:
                date_str, region, regional_manager, head_quarter, business_executive, agency, product, billed_qty, billed_rate, company_value,financial_year = row
                date_obj = datetime.datetime.strptime(date_str, '%m/%d/%Y')
                product_list.append(sales_data_OS(
                    Date=date_obj.date(),
                    Region=region,
                    Regional_manager=regional_manager,
                    Head_quarter=head_quarter,
                    Business_executive=business_executive,
                    Agency=agency,
                    Product=product,
                    Billed_qty=billed_qty,
                    Billed_rate=billed_rate,
                    Company_value=company_value,
                    financial_year=financial_year,
                ))

            sales_data_OS.objects.bulk_create(product_list)
            data["status"] = "sucessfully uploaded"
        except Exception as e:
            print(e)
            data["status"] = "uploading Failed"
    else:
        data["status"]="You are not Authorized to upload files to DataBase"        
    return Response(data)




# -------------------------------------------Monthly-API-----------------------------------------------
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def OS_monthly(request):
    data = {}
    try:
        queryset = sales_data_OS.objects.annotate(month=TruncMonth('Date')).values(
            'month').annotate(total_sales=Sum('Company_value')).order_by('month')
        serializer = OS_MonthlySerializer(queryset, many=True)
        data["status"] = serializer.data
    except Exception as e:
        print(e)
        data["status"] = "Error"
    return Response(data)




# -----------------------------------RM--BS-----API---------------------------------------------------


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def OS_pie(request):
    data = {}
    year = request.GET.get('year', None)
    if year == None:
        try:
            queryset = sales_data_OS.objects.values('Business_executive').annotate(
                total_sales=Sum("Company_value")).distinct()
            serializer = OSpieSerializer(queryset, many=True)
            data['status'] = serializer.data
        except Exception as e:
            print(e)
            data['status'] = "error"
    else:  
        try:
            queryset = sales_data_OS.objects.filter(financial_year = year).values('Business_executive').annotate(
                total_sales=Sum("Company_value")).distinct()
            serializer = OSpieSerializer(queryset, many=True)
            data['status'] = serializer.data
        except Exception as e:
            print(e)
            data['status'] = "error"      
    return Response(data)


# ---------------------------------------MAN--------------------------------------------------------------------


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def OS_Managers(request):
    data = {}
    try:
        sales_data = sales_data_OS.objects.values(
            'Regional_manager').distinct().order_by('Regional_manager')

        # print(sales_data)
        serializer = OS_ReginalManSerializer(sales_data, many=True)
        data['status'] = serializer.data
    except Exception as e:
        # print(e)
        data['status'] = "error"
    return Response(data)




# ----------------------------MON & Year--------------------------------


@api_view(['GET'])
def OS_year_month(request):
    data = []
    try:
        year = request.GET.get('year', None)
        month = request.GET.get('month', None)

        month_number = datetime.datetime.strptime(month, '%B').month
        queryset = sales_data_OS.objects.filter(Date__year=year, Date__month=month_number).values(
            'Business_executive').annotate(sales=Sum('Company_value'))
        for item in queryset:
            data.append(
                {'Business_executive': item['Business_executive'], 'sales': item['sales']})

    except Exception as e:
        data = []

    return Response(data)



# ------------------------------------Unique----Products---------------------Ap-------------------------------\
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def OS_unique_pro(request):
    data = []
    try:
        year = request.GET.get('year', None)
        month = request.GET.get('month', None)
        if month == None or year == None:
            qureyset = sales_data_OS.objects.values('Product').annotate(sales=Sum('Company_value'), TotalQty=Sum(
                "Billed_qty")).values('Product', "TotalQty", "sales").distinct().order_by('-TotalQty')
        else:
            month_number = datetime.datetime.strptime(month, '%B').month
            qureyset = sales_data_OS.objects.filter(Date__year=year, Date__month=month_number).values('Product').annotate(sales=Sum(
                'Company_value'), TotalQty=Sum("Billed_qty")).values('Product', "TotalQty", "sales").distinct().order_by('-TotalQty')
        for i in qureyset:
            data.append(i)
    except Exception as e:
        data = []

    return Response(data)





# ----------------------------------------Map---Cordinates----------------


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def OS_geolocation_view(request):
    data = {}
    try:
        queryset = OS_geolocation.objects.values(
            "Name", "Designation").distinct()
        for item in queryset:
            queryset2 = OS_geolocation.objects.filter(Name=item['Name']).values(
                'C_lat', 'C_lon', 'City', 'Designation', 'H_lat', 'H_lon', 'Head_quarters', 'P_lat', 'P_lon', 'Place', 'Type').distinct()
            # data[item['Name']] = list(queryset2)
            lis1 = []
            for i in queryset2:
                lis = {}
                lis['City'] = str(i['City'])+" "+str(i['Type'])
                lis['cityGeo'] = [i['C_lat'], i['C_lon']]
                lis['Head_quarters'] = i['Head_quarters']
                lis['HqGeo'] = [i['H_lat'], i['H_lon']]
                lis['Place'] = str(i['Place'])+" "+str(i['Type'])
                lis['PlaceGeo'] = [i['P_lat'], i['P_lon']]
                lis1.append(lis)
            data[str(item['Name'])+" -("+str(item['Designation'])+")"] = lis1
    except Exception as e:
        data = ["error"]
    return Response(data)



# --------------------------------AP_BE_SALES---------------------------------------------


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def OS_BE_mon_sales(request):
    res_data = {}
    test = []
    data = []
    try:
        unique_BE = sales_data_OS.objects.values(
            'Business_executive').distinct()
        queryset = sales_data_OS.objects.annotate(month=TruncMonth('Date')).values('month', 'Business_executive').annotate(
            total_sales=Sum('Company_value')).values('month', 'Business_executive', 'total_sales').order_by('month')
        for date in queryset:
            if date['month'] not in data:
                data.append(date['month'])

        for mn in data:
            set1 = {}
            for itm in queryset:
                if mn == itm['month']:
                    set1['month'] = mn
                    set1[itm['Business_executive']] = itm['total_sales']
            test.append(set1)
            # print(itm)
        be_list = []
        for i in unique_BE:
            be_list.append(i['Business_executive'])
        res_data["Business_executive"] = list(be_list)
        res_data["data"] = test

    except Exception as e:
        print(e)
    return Response(res_data)


#----------------------------------------delete---------------------------------------------

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_OS_DataBase(request):
    data={}
    if request.user.designation == "Manager":
        financial_year =request.GET.get("fin-year",None)
        if financial_year == None:
            try:
                sales_data_OS.objects.all().delete()
                data["status"]="succsess"
            except:
                data["status"]="Failed to delete"
        else:
            try:
                sales_data_OS.objects.filter(financial_year=financial_year).delete()
                data["status"]="succsess"
            except:
                data["status"]="Failed to delete"        
    else:
        data["status"]="You Dont have the Authorization to delete DataBase"
    return Response(data)




#----------------------------------------- Agency--Sales=-------------------------------------
@api_view(['GET'])
def OS_Agency_view(request):
    data = {}
    
    queryset = sales_data_OS.objects.annotate(month=TruncMonth('Date')).values('month', 'Business_executive', 'Agency').distinct()
    
    for entry in queryset:
        month = entry['month']
        business_executive = entry['Business_executive']
        agency = entry['Agency']
        
        if str(month) not in data:
            data[str(month)] = {}
        
        if business_executive not in data[str(month)]:
            data[str(month)][business_executive] = []
        
        data[str(month)][business_executive].append(agency)
    
    return Response(data)


# filtered result-----------------------

@api_view(['GET'])
def OS_agency_filtered_view(request):
    data=[]
    month = request.GET.get('month',None)
    business_executive = request.GET.get('be',None)
    agency = request.GET.get('agency',None)
    if agency != None and business_executive != None and month != None:
        try:
            queryset = sales_data_OS.objects.annotate(month=TruncMonth('Date')).filter(month=month,Business_executive=business_executive,Agency=agency).values('Date','Product','Billed_qty','Billed_rate')
            data=list(queryset)
        except Exception as e:
            print(e)
            data=[{e}]
    return Response(data)            


#-------------------------------------------------distinct-finantial-year----------
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def OS_distinct_finacial_year(request):
    data =[]
    try:
        queryset = sales_data_OS.objects.values('financial_year').distinct()
        for i in queryset:
            data.append(i['financial_year'])
    except :
        data=[]
    return Response(data)