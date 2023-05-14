from rest_framework import serializers
from .models import sales_data_AP
import datetime
class AP_SalesSerializer(serializers.ModelSerializer):
        
        
    class Meta:
        model = sales_data_AP
        fields = "__all__"
#--------------------------------------------------------------------------------------------------------------------------------------
class AP_MonthlySerializer(serializers.ModelSerializer):
    month = serializers.DateField(format='%m-%y')

    total_sales = serializers.DecimalField(max_digits=10, decimal_places=2)
   

    class Meta:
        model = sales_data_AP
        fields = ['month', 'total_sales']
#---------------------------------PIE---------------------------------------------------------
class APpieSerializer(serializers.ModelSerializer):
    total_sales=serializers.DecimalField(max_digits=10,decimal_places=2, coerce_to_string=False)

    class Meta:
        model =sales_data_AP
        fields =['Business_executive','total_sales']

#----------------------------------------------------------------------------------------------------------
class AP_ReginalManSerializer(serializers.ModelSerializer):
    business_executives = serializers.SerializerMethodField()

    class Meta:
        model = sales_data_AP
        fields = ['Regional_manager', 'business_executives']

    def get_business_executives(self, obj):
        business_executives_data = sales_data_AP.objects.filter(
            Regional_manager=obj['Regional_manager']
        ).values('Business_executive').distinct()

        return [item['Business_executive'] for item in business_executives_data]
   