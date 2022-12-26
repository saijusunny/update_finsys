from django import forms
from .models import *
from .models import noninventory

class ImageForm(forms.ModelForm):
    class Meta:
        model = service
        fields = ['img', 'name', 'sku', 'sac', 'unit','categ','descr','check1','saleprice','income','check2','tax','abatement','sertype']


class ImageForm2(forms.ModelForm):
    class Meta:
        model=noninventory
        fields=("image","name","sku","hsn","unit","category","initialqty","date","stockalrt","invacnt","description","salesprice","incomeacnt","tax","purchaseinfo","cost","expacnt","purtax","revcharge","presupplier",)


class ImageForm3(forms.ModelForm):
    class Meta:
        model = bundle
        fields = ['image', 'name', 'sku', 'description']

class ImageForm4(forms.ModelForm):
    class Meta:
        model=inventory
        fields=("image","name","sku","hsn","unit","category","initialqty","date","stockalrt","invacnt","description","salesprice","incomeacnt","tax","purchaseinfo","cost","expacnt","purtax","revcharge","presupplier")
