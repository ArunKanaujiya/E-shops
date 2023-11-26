from django.shortcuts import render,redirect
from django.http import HttpResponse
from WebApp.models.product import Product
from WebApp.models.category import Category
from WebApp.models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponse
from django.views import View

# Create your views here.
class index(View):
    def post(self,request):
        product=request.POST.get('product')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                cart[product]=quantity+1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1


        request.session['cart']=cart
        print(request.session['cart'])
        return redirect('index')



    def get(self,request):
        products=None
        #request.session.clear('cart')
        categories=Category.objects.all()
        category_id=request.GET.get('category')
        if category_id:
            products=Product.get_all_products_by_id(category_id)
        else:
            products=Product.get_all_products()
            print(request.GET)

            context={'products':products,'categories':categories}
            return render(request,'myapp/index.html',context)

def validatecustomer(customer):
    error_message=None
    if not customer.first_name:
        error_message="firts name is requird"
    elif len(customer.first_name) < 4:
        error_message='name must be 4 character'
    elif not customer.last_name:
        error_message='last name is requeired'
    elif len(customer.last_name) < 4:
        error_message='last name nust be 4 character long'
    elif not customer.phone:
        error_message='phone number is requeired'
    elif len(customer.phone) < 10:
        error_message='phone number must be 10 char long'
    elif not customer.email:
        error_message='email is requeired'
    elif len(customer.email) < 10:
        error_message='email must be 10 char long'
    elif not customer.password:
        error_message='password is requeired'
    elif len(customer.password) < 5:
        error_message='password must be special char long'

    elif customer.isexists():
        error_message='email address already register'

    return error_message
        




def update(request,slug):
    queryset=Product.objects.get(productslug=slug)
    if request.method=='POST':
        data=request.POST
        name=data.get('name')
        price=data.get('price')
        description=data.get('description')
        image=request.FILES.get('image')
        queryset.name=name
        queryset.price=price
        queryset.description=description
        if image:
            queryset.image=image
        
        queryset.save()
        return redirect('/index')

    context={'queryset':queryset}
    return render(request,'myapp/update.html',context)

def registeruser(request):
    data=request.POST
    first_name=data.get('firstname')
    last_name=data.get('lastname')
    phone=data.get('phone')
    email=data.get('email')
    password=data.get('password')

    value={
            'first_name':first_name,
            'last_name':last_name,
            'phone':phone,
            'email':email,
            'password':password
        }
    error_message=None

    customer=Customer(first_name=first_name,
                         last_name=last_name,
                         phone=phone,
                         email=email,
                         password=password)

    error_message=validatecustomer(customer)
    if not error_message:
        print(first_name,last_name,phone,email,password)
        customer.password=make_password(queryset.password)
           
        customer.save()
        return redirect('/index')
    else:
        return render(request,'myapp/signup.html',{'error':error_message,'values':value})




def signup(request):
    if request.method=='GET':
        return render(request,'myapp/signup.html')
    else:
        return registeruser(request)
        

def login_page(request):
    if request.method=='GET':
        return render(request,'myapp/login.html')
    else:
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)
        print(customer)
        error_message=None
        if customer:
            flag=check_password(password,customer.password)
            if flag:
                request.session['customer']=customer.id
                request.session['customer']=customer.email

                return redirect('/index')
            else:
                error_message='email or password invalid'
        else:
            error_message='email or password invalid'
        print(email,password)
        print('you are :',request.session.get('email'))
        return render(request,'myapp/login.html',{'error':error_message})
