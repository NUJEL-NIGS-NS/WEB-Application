from django.db import models

# Create your models here.


class sales_data_OS(models.Model):
    Date = models.DateField(blank=True)
    Region = models.CharField(max_length=30)
    Regional_manager = models.CharField(max_length=30)
    Head_quarter = models.CharField(max_length=30)
    Business_executive = models.CharField(max_length=30)
    Agency = models.CharField(max_length=200)
    Product = models.CharField(max_length=60)
    Billed_qty = models.IntegerField()
    Billed_rate = models.DecimalField(max_digits=100, decimal_places=2)
    Company_value = models.DecimalField(max_digits=100, decimal_places=2)
    financial_year = models.IntegerField(default=2022)

    def __str__(self):
        return str(self.Date) + "  "+self.Business_executive


class OS_geolocation(models.Model):
    Designation =models.CharField(max_length=30)
    Name = models.CharField(max_length=30)
    Head_quarters = models.CharField(max_length=30)
    Place = models.CharField(max_length=30)
    City = models.CharField(max_length=30)
    P_lat = models.DecimalField(max_digits=10,decimal_places=7) 
    P_lon = models.DecimalField(max_digits=10,decimal_places=7)
    C_lat = models.DecimalField(max_digits=10,decimal_places=7)
    C_lon = models.DecimalField(max_digits=10,decimal_places=7)
    H_lat =models.DecimalField(max_digits=10,decimal_places=7)
    H_lon = models.DecimalField(max_digits=10,decimal_places=7)
    Type =models.CharField(max_length=10)

    def __str__(self):
        return self.Name +" "+ self.Head_quarters
    
