from django.db import models
from TodoApp.models import Product

# Create your models here.
class Cart(models.Model):
    user=models.CharField(max_length=200)
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    class Meta:
        db_table='cart'
        
    # def __str__(self):
    #     return self.Product    