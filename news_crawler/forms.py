from django import forms

class AddNewsForm(forms.Form):
    crawlerName = forms.CharField(label='Crawler Name:', required=True)
    site = forms.CharField(label="Site:", required=True)
    startDate = forms.CharField(label="Start Date:", required=True)

class EditNewsForm(forms.Form):
    crawlerName = forms.CharField(label='Crawler Name:', required=True)
    site = forms.CharField(label="Site:", required=True)
    startDate = forms.CharField(label="Start Date:", required=True)