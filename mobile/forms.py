from django.forms import ModelForm
from .models import Product
from django import forms

class ProductCreateForm(ModelForm):
    class Meta:
        model=Product
        fields="__all__"
        widgets={
            "mobile_name":forms.TextInput(attrs={"class":"form-control p-2"}),
            "price": forms.TextInput(attrs={"class": "form-control p-2"}),
            "specs": forms.Textarea(attrs={"class": "form-control p-2"})

        }


    def clean(self):
        cleaned_data=super().clean()
        price=cleaned_data.get("price")
        if price<500:
            msg="invalid price"
            self.add_error("price",msg)