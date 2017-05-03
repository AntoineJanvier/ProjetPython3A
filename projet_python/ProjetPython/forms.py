from django import forms


class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=255, label="Titre de l'image")
    file = forms.FileField(label="Choisir un fichier")
