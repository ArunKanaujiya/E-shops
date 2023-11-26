from django.db import models

class Customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=13)
    email=models.EmailField(null=True,max_length=50,unique=True)
    password=models.CharField(max_length=100)


    def register(self):
        self.save()

    
    def isexists(self):
        if Customer.objects.get(email=self.email):
            return True
        return False

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.filter(email=email)
        except:
            return False