from django import forms

class ChatUploadForm(forms.Form):
    chat_file = forms.FileField(label='Select a chat file to upload')