from django import forms
from .models import Img


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Img
        fields = ('name', 'file')
    name = forms.CharField(max_length=255, label="Titre de l'image")
    file = forms.FileField(label="Choisir un fichier")
