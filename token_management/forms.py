from django import forms

class AddTokenForm(forms.Form):
    tokenName = forms.CharField(label='Token Name:', required=True)
    consumerKey = forms.CharField(label='Consumer Key:', required=True)
    consumerSecret = forms.CharField(label='Consumer Secret:', required=True)
    accessKey = forms.CharField(label='Access Key:', required=True)
    accessSecret = forms.CharField(label='Access Secret:', required=True)

class EditTokenForm(forms.Form):
    tokenName = forms.CharField(label='Token Name:', required=True)
    consumerKey = forms.CharField(label='Consumer Key:', required=True)
    consumerSecret = forms.CharField(label='Consumer Secret:', required=True)
    accessKey = forms.CharField(label='Access Key:', required=True)
    accessSecret = forms.CharField(label='Access Secret:', required=True)
