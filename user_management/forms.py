from django import forms

class AddUserForm(forms.Form):
    attrs = {
        'class': 'form-control',
        'type' : 'text'
    }

    pass_attrs = {
        'class': 'form-control',
        'type': 'password'
    }

    username = forms.CharField(label="Username:", required=True, widget=forms.TextInput(attrs=attrs))
    fullname = forms.CharField(label="FullName:")
    password = forms.CharField(label="Initial Password:", required=True, widget=forms.TextInput(attrs=pass_attrs))

class EditUserForm(forms.Form):
    attrs = {
        'class': 'form-control',
        'type' : 'text'
    }

    pass_attrs = {
        'class': 'form-control',
        'type': 'password'
    }

    userid = forms.CharField(label="UserID:")
    username = forms.CharField(label="Username:", required=True, widget=forms.TextInput(attrs=attrs))
    name = forms.CharField(label="Name:")
    password = forms.CharField(label="Password:", required=True, widget=forms.TextInput(attrs=pass_attrs))