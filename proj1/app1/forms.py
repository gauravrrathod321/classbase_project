from .models import Product
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    widgets = {
        "product_name":forms.TextInput(attrs={'class':"form-control"}),
        "prodcut_price" :forms.NumberInput(attrs={'class':"form-control"}),
        "product_quan":forms.TextInput(attrs={'class':"form-control"}),
        "delivery_address":forms.Textarea(attrs={'class':"form-control"}),
        "payment_mode":forms.Select(attrs={'class':"form-control"})
    }