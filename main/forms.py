from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django import forms
from main.models import AllProductModel,ReviewModel,ContactUsModel,Ordering


class RegisterForm(UserCreationForm):
        class Meta:
            model=User
            fields=['username','last_name','email','password1','password2']

class AddProductForm(forms.ModelForm):
    class Meta:
        model=AllProductModel
        fields=['cate','img','name','price_old','price_now','info','img1','img2','email']

class ReviewForm(forms.ModelForm):
     class Meta:
          model=ReviewModel
          fields=['name','surname','comment','img','rate']


class ContactUsForm(forms.ModelForm):
     class Meta:
          model=ContactUsModel
          fields=['name','email','subject','message']

class OrderForm(forms.ModelForm):
     class Meta:
          model=Ordering
          fields=['name','phone']
