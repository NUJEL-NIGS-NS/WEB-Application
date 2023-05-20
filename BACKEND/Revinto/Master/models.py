from django.db import models

# Create your models here.
class MasterStates(models.Model):
    State = models.CharField(max_length=30)
    Path = models.CharField(max_length=10,default='AP')

    def __str__(self):
        return self.State
    
