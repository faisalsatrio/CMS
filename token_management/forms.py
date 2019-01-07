from django import forms

class AddTokenForm(forms.Form):
    topic_attrs =(
        ('Pilpres 2019','Pilpres 2019'),
        ('Pil kb','Pil kb'),
    )

    platform_attrs =(
        ('twitter','twitter'),
        ('facebook','facebook'),
        ('instagram','instagram'),
        ('youtube','youtube'),
    )

    token_attrs =(
        ('token1','token1'),
        ('token2','token2'),
        ('token3','token3'),
    )

    topic = forms.ChoiceField(label='Topic:', required=True, choices=topic_attrs)
    subject = forms.CharField(label="Subject:")
    keyword = forms.CharField(label="Keyword:")
    platform = forms.ChoiceField(label='Platform:', required=True, choices=platform_attrs)
    token = forms.ChoiceField(label='Token:', choices=token_attrs)

class EditTokenForm(forms.Form):
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

    token_attrs =(
        ('token1','token1'),
        ('token2','token2'),
        ('token3','token3'),
    )

    topic = forms.ChoiceField(label='Topic:', required=True, choices=topic_attrs)
    subject = forms.CharField(label="Subject:")
    keyword = forms.CharField(label="Keyword:")
    platform = forms.ChoiceField(label='Platform:', required=True, choices=platform_attrs)
    token = forms.ChoiceField(label='Token:', choices=token_attrs)
