from django import forms

# Form for creating a listing
class createForm (forms.Form):
    title = forms.CharField(label="Your item name", max_length=200)
    desc = forms.CharField(label="Description of the item", max_length=500)
    floor_price = forms.CharField(label="Minimum Price")
    photo_url = forms.URLField()
    date_end = forms.DateField()
    
    def clean_photo_url(self):
        photo_url = self.cleaned_data['photo_url'].strip()
        return photo_url