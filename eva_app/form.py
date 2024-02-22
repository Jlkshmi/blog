from django import forms
from django.contrib.auth.forms import UserCreationForm

from eva_app.models import Login, Customer, Publisher, Blog


class Login_Form(UserCreationForm):
    class Meta:
        model= Login
        fields=('username','password1','password2')

class Customer_Form(forms.ModelForm):
    class Meta:
        model=Customer
        fields=('name','contact_no','email',)

class Publisher_Form(forms.ModelForm):
    class Meta:
        model= Publisher
        fields=('name','contact_no','email',)

class Blog_Form(forms.ModelForm):
    class Meta:
        model= Blog
        fields=('title','content','name','email','upload_pic',)