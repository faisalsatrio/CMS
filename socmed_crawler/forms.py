from django import forms

class AddSubjectForm(forms.Form):
    topic_attrs =(
        ('Pilpres 2019','Pilpres 2019'),
        ('abc','abc'),
        ('def','def'),
    )

    platform_attrs =(
        ('Twitter','Twitter'),
        ('abc','abc'),
        ('def','def'),
    )

    topic = forms.ChoiceField(label='Topic:', required=True, choices=topic_attrs)
    subject = forms.CharField(label="Subject:")
    keyword = forms.CharField(label="Keyword:")
    platform = forms.ChoiceField(label='Platform:', required=True, choices=platform_attrs)

class EditSubjectForm(forms.Form):
    topic_attrs =(
        ('Pilpres 2019','Pilpres 2019'),
        ('abc','abc'),
        ('def','def'),
    )

    platform_attrs =(
        ('Twitter','Twitter'),
        ('abc','abc'),
        ('def','def'),
    )

    topic = forms.ChoiceField(label='Topic:', required=True, choices=topic_attrs)
    subject = forms.CharField(label="Subject:")
    keyword = forms.CharField(label="Keyword:")
    platform = forms.ChoiceField(label='Platform:', required=True, choices=platform_attrs)
