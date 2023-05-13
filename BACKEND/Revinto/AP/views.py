from .models import sales_data_AP
from .serializer import AP_SalesSerializer,AP_MonthlySerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response
import datetime
from django.db.models.functions import TruncMonth,TruncYear
from django.db.models import Sum
import csv
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage(location='/temp')

# authentication
# models
# Create your views here.

#---------------------------------------update-API-------------------------------------------------------
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_db_AP(request):
    data = {}
    try:
        file = request.FILES["file"]
        content = file.read()
        file_content = ContentFile(content)
        file_name = fs.save("tmp.csv", file_content)
        tmp_file = fs.path(file_name)
        csv_file = open(tmp_file, errors="ignore")
        reader = csv.reader(csv_file)
        next(reader)

        product_list = []

        for row in reader:
            date_str, region, regional_manager, head_quarter, business_executive, agency, product, billed_qty, billed_rate, company_value = row
            date_obj = datetime.datetime.strptime(date_str, '%m/%d/%Y')
            product_list.append(sales_data_AP(
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
            ))

        sales_data_AP.objects.bulk_create(product_list)
        data["status"] = "sucessfully uploaded"
    except Exception as e:
        # print(e)
        data["status"] = "uploading Failed"
    return Response(data)


#-------------------------------------------Monthly-API-----------------------------------------------
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def AP_monthly(request):
    data = {}
    try:
        queryset = sales_data_AP.objects.annotate(month=TruncMonth('Date')).values('month').annotate(total_sales=Sum('Company_value')).order_by('month')
        serializer =AP_MonthlySerializer(queryset,many=True)
        data["status"] =serializer.data
    except Exception as e:
        print(e)
        data["status"] ="Error"
    return Response(data)    
