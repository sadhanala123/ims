from django import forms
from .models import Add_brand, Add_product, Add_purchase ,Add_orders,Add_customer

class Add_brandForm(forms.ModelForm):
    class Meta:
        model = Add_brand
        fields = ['brand_name','Category_name','Status']
        widgets = {
            'brand_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Category_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Status': forms.TextInput(attrs={'class': 'form-control'}),

        }

class Add_productForm(forms.ModelForm):
    class Meta:
        model = Add_product
        fields = ['Category_name','brand_name','product_name','product_model','product_description','product_quantity','product_base_price','product_tax','supplier_name']
        widgets = {
            'Category_name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand_name': forms.TextInput(attrs={'class': 'form-control'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'product_model': forms.TextInput(attrs={'class': 'form-control'}),
            'product_description': forms.TextInput(attrs={'class': 'form-control'}),
            'product_quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'product_base_price': forms.TextInput(attrs={'class': 'form-control'}),
            'product_tax': forms.TextInput(attrs={'class': 'form-control'}),
            'supplier_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Add_purchaseForm(forms.ModelForm):
    class Meta:
        model = Add_purchase
        fields = ['product_name','product_quantity','supplier_name']
        widgets={
        'product_name': forms.TextInput(attrs={'class': 'form-control'}),
        'product_quantity': forms.TextInput(attrs={'class': 'form-control'}),
        'supplier_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class Add_ordersForm(forms.ModelForm):
    class Meta:
        model = Add_orders
        fields = ['product_name','total_item','Name']
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'total_item': forms.TextInput(attrs={'class': 'form-control'}),
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class Add_customer(forms.ModelForm):
      class Meta:
          model=Add_customer
          fields=['Name','mobile','balance','Address']
          widgets = {
              'Name': forms.TextInput(attrs={'class': 'form-control'}),
              'mobile': forms.TextInput(attrs={'class': 'form-control'}),
              'balance': forms.TextInput(attrs={'class': 'form-control'}),
              'Address': forms.TextInput(attrs={'class': 'form-control'}),
          }
