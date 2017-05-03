from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .models import Img
from PIL import Image
from django.conf import settings


def home(request):
    title = "Home"
    images = Img.objects.filter(style="ORIGINAL")
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
            up = Img.objects.create()
            up.name = form.cleaned_data['name']
            up.file = form.cleaned_data['file']
            up.save()
            return HttpResponseRedirect('/success')
    else:
        form = UploadFileForm()
        form.fields['name'].widget.attrs = {'class': 'form-control'}
        form.fields['file'].widget.attrs = {'class': 'form-control'}
    return render(request, 'upload.html', locals())


def compute_image(request, id):
    title = "Compute image"
    img = Img.objects.get(id=id)
    im = Image.open(img.file.path)

    cop = im.copy()
    w, h = cop.size
    pix = cop.load()
    for i in range(0, w-10):
        for j in range(0, h-10):
            r, g, b = pix[i, j]
            r = 255 - r
            g = 255 - g
            b = 255 - b
            pix[i,j] = r, g, b
    cop.save(img.file.path.split('.')[0] + "_inverted." + img.file.path.split('.')[1])
    im_inverted_url = img.file.url.split('.')[0] + "_inverted." + img.file.url.split('.')[1]

    w, h = im.size
    gray = Image.new("L", (w, h))
    pix2 = gray.load()

    cop = im.copy()
    pix = cop.load()
    w, h = cop.size
    for i in range(0, w):
        for j in range(0, h):
            r, g, b = pix[j, i]
            sum = int((r + g + b) / 3)
            pix2[j, i] = sum

    cop.save(img.file.path.split('.')[0] + "_gray." + img.file.path.split('.')[1])
    im_gray_url = img.file.url.split('.')[0] + "_gray." + img.file.url.split('.')[1]

    return render(request, 'compute_image.html', locals())

