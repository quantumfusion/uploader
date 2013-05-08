from django import forms

class FileUploadForm(forms.Form):
    qqfile = forms.FileField()
