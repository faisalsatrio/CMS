from django import forms

class TopicForm(forms.Form):
    topicName = forms.CharField(label='Topic:', required=True)
    clientName = forms.CharField(label="Client:", required=True)
    description = forms.CharField(label="Description:", required=True)
