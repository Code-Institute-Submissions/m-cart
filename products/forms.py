from django import forms

from .models import Product

class ProductAdd_Form(forms.ModelForm):
    class Meta:
        model=Product
        fields= '__all__'
        
# class ProductCategoriesForm(forms.ModelForm):
#     class Meta:
#         model=ProductCategories
#         fields= '__all__'
