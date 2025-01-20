from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000, widget=forms.Textarea)