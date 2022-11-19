from django.db import models

# Create your models here.
class Product(models.Model):
    Prod_id = models.AutoField
    prod_name = models.CharField(max_length=30)
    desc = models.CharField(max_length=50)
    pub_date = models.DateField()
    catagory = models.CharField(max_length=50,default='')
    subcatagory = models.CharField(max_length=50,default='')
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop/static',default='')

    def __str__(self):
        return self.prod_name

    
    
