from django import forms
from products.models import Tag, Category

# Query form to filter by description, tag and category
class ProductFilterForm(forms.Form):
    query = forms.CharField(label="Search by Description", max_length=300, required=False, widget=forms.TextInput(attrs={'onchange': 'submit();'}))
    tag = forms.ModelChoiceField(label="Tags", queryset=Tag.objects.all(), required=False, widget=forms.Select(attrs={'onchange': 'submit();'}))
    category = forms.ModelChoiceField(label="Categories", queryset=Category.objects.all(), required=False, widget=forms.Select(attrs={'onchange': 'submit();'}))