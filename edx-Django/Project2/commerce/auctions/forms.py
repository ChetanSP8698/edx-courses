from django import forms

Categories = [
    ('FS', 'Fashion'),
    ('EC', 'Electronics'),
    ('BE', 'Beauty'),
    ('HF', 'Home & Furniture'),
    ('SP', 'Sports'),
    ('BK', 'Books'),
    ('CR', 'Cars'),
    ('OT', 'Others')
]

class listing_form(forms.Form):
    title = forms.CharField(label='Title', max_length=64)
    descr = forms.CharField(
        label='Description', 
        max_length=512, 
        widget=forms.Textarea(attrs={'rows':5, 'cols':50}),
    )
    image = forms.URLField(label='Image URL', required=False)
    category = forms.ChoiceField(required=False, label='Category', choices=Categories)
    bid = forms.FloatField(label='Starting Bid')