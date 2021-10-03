from django import forms

class ShortenerForm(forms.Form):
    alias = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '(optional)'}), required=False)
    long_url = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'http://example.com'}))
