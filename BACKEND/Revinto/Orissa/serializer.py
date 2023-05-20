from rest_framework import serializers
from .models import sales_data_OS
import datetime

class OS_SalesSerializer(serializers.ModelSerializer):
        
        
    class Meta:
        model = sales_data_OS
        fields = "__all__"
#--------------------------------------------------------------------------------------------------------------------------------------
class OS_MonthlySerializer(serializers.ModelSerializer):
    month = serializers.DateField(format='%m-%y')

    total_sales = serializers.DecimalField(max_digits=10, decimal_places=2)
   

    class Meta:
        model = sales_data_OS
        fields = ['month', 'total_sales']
#---------------------------------PIE---------------------------------------------------------
class OSpieSerializer(serializers.ModelSerializer):
    total_sales=serializers.DecimalField(max_digits=10,decimal_places=2, coerce_to_string=False)

    class Meta:
        model =sales_data_OS
        fields =['Business_executive','total_sales']

#----------------------------------------------------------------------------------------------------------
class OS_ReginalManSerializer(serializers.ModelSerializer):
    business_executives = serializers.SerializerMethodField()

    class Meta:
        model = sales_data_OS
        fields = ['Regional_manager', 'business_executives']

    def get_business_executives(self, obj):
        business_executives_data = sales_data_OS.objects.filter(
            Regional_manager=obj['Regional_manager']
        ).values('Business_executive').distinct()

        return [item['Business_executive'] for item in business_executives_data]
   