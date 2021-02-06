from django import forms
# from django.db import models
# from django.forms import ModelForm
from .models import Product

class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = [
      'title', 
      'price',
      'summary', 
      'featured',
    ] 

def clean_title(self, *args, **kwargs):
  title = self.cleaned_data.get('title')
  if not 'CFE' in title:
    raise forms.ValidationError('This is not a valid title')
  else: 
    return title

class RawProductForm(forms.Form):
  title = forms.CharField(label='title')
  price = forms.DecimalField(initial=1.99)
  summary = forms.CharField(required=False, widget=forms.Textarea)

