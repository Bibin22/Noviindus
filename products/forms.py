from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *




class ProductAdd(ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        widgets = {

            'product_name': forms.TextInput(attrs={'class': 'form-control', 'required':'true'}),
            'product_description': forms.Textarea(attrs={'class': 'form-control'}),
            'product_status': forms.Select(attrs={'class': 'form-control', 'required':'true'}),
            'product_category': forms.Select(attrs={'class': 'form-control', 'required':'true'}),
            'product_prize': forms.TextInput(attrs={'class': 'form-control','type':'number', 'required':'true'}),
            'product_image': forms.FileInput(attrs={'required': 'true'}),


        }
