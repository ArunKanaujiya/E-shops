from django.db import models
from WebApp.models.category import Category
from autoslug import AutoSlugField

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=200,default='')
    image=models.ImageField(upload_to='products')
    productslug=AutoSlugField(populate_from='name',unique=True,null=True,default=None)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()


    
