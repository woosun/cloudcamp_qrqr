from django import forms
from .models import product

#사용자들에게 입력받기위한틀
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('uid','category','name','imgsrc','display_yn','query_yn','query_data','create_date')
        widgets = {'id' : forms.HiddenInput()}
