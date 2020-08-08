from django import forms
from .models import listings, Categories

'''
class listing_form(forms.ModelForm):
    class Meta:
        model = listings
        fields = ["item_title", "item_des", "item_image", "item_category", "item_price"]
'''

class listing_form(forms.Form):
    title = forms.CharField(label='Title  ', max_length=64)
    descr = forms.CharField(
        label='Description  ', 
        max_length=512, 
        widget=forms.Textarea(attrs={'rows':5, 'cols':30}),
    )
    image = forms.URLField(label='Image URL  ', required=False)
    category = forms.ChoiceField(required=False, label='Category  ', choices=Categories)
    price = forms.FloatField(label='Pricing ')
    bid = forms.FloatField(label='Starting Bid  ')