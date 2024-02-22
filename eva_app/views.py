from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from eva_app.form import Login_Form, Customer_Form, Publisher_Form, Blog_Form


# Create your views here.
def front_page(request):
    return render(request,'front_page.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('')
            elif user.is_customer:
                return redirect('')
            elif user.is_publisher:
                return redirect('')
        else:
                messages.info(request,'Invalid Credentials')
    return render(request,'login_page.html')


def customer_reg(request):
    form1=Login_Form()
    form2=Customer_Form()
    if request.method == 'POST':
        form1 = Login_Form(request.POST)
        form2 = Customer_Form(request.POST)

        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_customer = True
            user.save()
            user1 = form2.save(commit=False)
            user1.user = user
            user1.save()
            return redirect('login_view')
    return render(request,'cus_reg.html',{'form1':form1,'form2':form2})


def publisher_reg(request):
    form1=Login_Form()
    form2= Publisher_Form()
    if request.method == 'POST':
        form1 = Login_Form(request.POST)
        form2 = Publisher_Form(request.POST, request.FILES)

        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user. is_publisher = True
            user.save()
            user1 = form2.save(commit=False)
            user1.user = user
            user1.save()
            return redirect('login_view')
    return render(request,'pub_reg.html',{'form1':form1,'form2':form2})


def blog_create(request):
    form1 = Blog_Form()
    if request.method == 'POST':
        form1= Blog_Form(request.POST,request.FILES)
        if form1.is_valid():
            form2=form1.save(commit=False)
            form2.save()
            return redirect('')
    return render(request,'blog_create.html',{'form1':form1})



