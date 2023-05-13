from django.db import models

# Create your models here.


class sales_data_AP(models.Model):
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

    def __str__(self):
        return str(self.Date) + "  "+self.Business_executive
