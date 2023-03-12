from django.db import models

# Create your models here.
from django.db import  models

class Product(models.Model):  #類別屬性
    id = models.IntegerField(primary_key=True) #整數-->主鰎 不可重複
    name = models.CharField(max_length=40) #字串最多40字
    price = models.IntegerField()
    img = models.CharField(max_length=40)

    def __str__(self):
        pd = f'{self.id} {self.name} {self.price} {self.img}'
        return pd