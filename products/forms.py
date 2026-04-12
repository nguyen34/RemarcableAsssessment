from django import forms
from products.models import Tag, Category

class ProductFilterForm(forms.Form):
    query = forms.CharField(label="Search by Description", max_length=300, required=False)
    tag = forms.ModelChoiceField(label="Tags", queryset=Tag.objects.all(), required=False)
    category = forms.ModelChoiceField(label="Categories", queryset=Category.objects.all(), required=False)