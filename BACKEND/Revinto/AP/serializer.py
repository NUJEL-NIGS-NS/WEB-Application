from rest_framework import serializers
from .models import sales_data_AP

class AP_SalesSerializer(serializers.ModelSerializer):
        
        
    class Meta:
        model = sales_data_AP
        fields = "__all__"

class AP_MonthlySerializer(serializers.ModelSerializer):
    month = serializers.DateField(format='%m-%y')

    total_sales = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = sales_data_AP
        fields = ['month', 'total_sales']
