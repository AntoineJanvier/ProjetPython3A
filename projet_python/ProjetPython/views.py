from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .models import Image
from django.conf import settings


def home(request):
    title = "Home"
    images = Image.objects.filter(style="ORIGINAL")
    MEDIA_BASE = settings.MEDIA_URL
    return render(request, "home.html", locals())


def galery(request):
    title = "Galery"
    return render(request, "galery.html", locals())


def upload(request):
    title = "Upload"
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        form.fields['name'].widget.attrs = {'class': 'form-control'}
        form.fields['file'].widget.attrs = {'class': 'form-control'}
        if form.is_valid():
            up = Image.objects.create()
            up.name = form.cleaned_data['name']
            up.file = form.cleaned_data['file']
            up.save()
            return HttpResponseRedirect('/success')
    else:
        form = UploadFileForm()
        form.fields['name'].widget.attrs = {'class': 'form-control'}
        form.fields['file'].widget.attrs = {'class': 'form-control'}
    return render(request, 'upload.html', locals())


def compute_image(request):
    title = "Compute image"
    return render(request, 'compute_image.html', locals())