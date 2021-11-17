from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    ''' creates a product form for use on html pages in product app'''
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [
            (cat.id, cat.get_friendly_name())
            for cat in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-1'