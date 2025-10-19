from django.db import models

class Inventory(models.Model):
    name=models.CharField(max_length=100)
    description= models.CharField
    quantity= models.IntegerField
    price=models.FloatField
    createdat= models.DateTimeField
    Updatedat= models.DateTimeField

    def __str__(self):
        return f"{self.name} ({self.description})"