from rest_framework import serializers
from .models import sales_data_KL
import datetime
class KL_SalesSerializer(serializers.ModelSerializer):
        
        
    class Meta:
        model = sales_data_KL
        fields = "__all__"
#--------------------------------------------------------------------------------------------------------------------------------------
class KL_MonthlySerializer(serializers.ModelSerializer):
    month = serializers.DateField(format='%m-%y')

    total_sales = serializers.DecimalField(max_digits=10, decimal_places=2)
   

    class Meta:
        model = sales_data_KL
        fields = ['month', 'total_sales']
#---------------------------------PIE---------------------------------------------------------
class KLpieSerializer(serializers.ModelSerializer):
    total_sales=serializers.DecimalField(max_digits=10,decimal_places=2, coerce_to_string=False)

    class Meta:
        model =sales_data_KL
        fields =['Business_executive','total_sales']

#----------------------------------------------------------------------------------------------------------
class KL_ReginalManSerializer(serializers.ModelSerializer):
    business_executives = serializers.SerializerMethodField()

    class Meta:
        model = sales_data_KL
        fields = ['Regional_manager', 'business_executives']

    def get_business_executives(self, obj):
        business_executives_data = sales_data_KL.objects.filter(
            Regional_manager=obj['Regional_manager']
        ).values('Business_executive').distinct()

        return [item['Business_executive'] for item in business_executives_data]
   