from django import forms

# Form for creating a listing
class createForm (forms.Form):
    CATEGORY_CHOICES = (
        ('jewelry', 'Jewelry'),
        ('NFTs', 'NFTs'),
        ('fashion', 'Fashion'),
        ('home', 'Home'),
    )
    title = forms.CharField(label="Your item name", max_length=200)
    desc = forms.CharField(label="Description of the item", max_length=500)
    floor_price = forms.CharField(label="Minimum Price")
    photo_url = forms.URLField()
    date_end = forms.DateField(label="End date (MM/DD/YYYY)")
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label="Category")
    
    def clean_photo_url(self):
        photo_url = self.cleaned_data['photo_url'].strip()
        return photo_url