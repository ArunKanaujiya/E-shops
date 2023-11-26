from django.contrib import admin
from WebApp.models.category import Category
from WebApp.models.product import Product
from WebApp.models.customer import Customer

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','category']


class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']


class CustomerAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','phone','email','password']


admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Customer,CustomerAdmin)