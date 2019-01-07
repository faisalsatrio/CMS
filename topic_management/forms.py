from django import forms

class AddTopicForm(forms.Form):
    topicName = forms.CharField(label='Topic:', required=True)
    clientName = forms.CharField(label="Client:", required=True)
    description = forms.CharField(label="Description:", required=True)

class EditTopicForm(forms.Form):
    topicName = forms.CharField(label='Topic:', required=True)
    clientName = forms.CharField(label="Client:", required=True)
    description = forms.CharField(label="Description:", required=True)
