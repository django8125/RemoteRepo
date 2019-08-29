from django import forms
from .models import ProductData
class ProductForm(forms.Form):
    product_id=forms.IntegerField(
        label="Enter Your Product id",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Id'
            }
        )
    )
    product_name=forms.CharField(
        label="Enter Your Product Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product name'
            }
        )
    )
    product_cost=forms.IntegerField(
        label="Enter Your Product Cost",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Cost'
            }
        )
    )
    product_color=forms.CharField(
        label="Enter Your Product Color",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Color'
            }
        )
    )
    product_class=forms.CharField(
        label="Enter Your Product Class",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Class'
            }
        )
    )
class Productupdateform(forms.Form):
    product_id=forms.IntegerField(
        label="Enter Your Product Id",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Id'
           }
        )
    )
    product_cost=forms.IntegerField(
        label="Enter Your Product cost",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product cost'
            }
        )
    )
class Productdeleteform(forms.Form):
    product_id=forms.IntegerField(
        label="Enter the product id",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Id'
            }
        )
    )