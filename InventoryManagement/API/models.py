from django.db import models

class Inventory(models.Model):
    name=models.CharField
    description= models.CharField
    quantity= models.IntegerField
    price=models.FloatField
    createdat= models.DateTimeField
    Updatedat= models.DateTimeField
