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


    ##
    # TODO : Split onto modules
    ##
    # INVERTED COLORS
    #
    cop = im.copy()
    w, h = cop.size
    pix = cop.load()
    for i in range(0, w):
        for j in range(0, h):
            r, g, b = pix[i, j]
            r = 255 - r
            g = 255 - g
            b = 255 - b
            pix[i, j] = r, g, b
    cop.save(img.file.path.split('.')[0] + "_inverted." + img.file.path.split('.')[1])
    im_inverted_url = img.file.url.split('.')[0] + "_inverted." + img.file.url.split('.')[1]

    # SHADES OF GREY
    #
    w, h = im.size
    gray = Image.new("L", (w, h))
    pix2 = gray.load()

    cop = im.copy()
    pix = cop.load()
    w, h = cop.size
    for i in range(0, w):
        for j in range(0, h):
            r, g, b = pix[i, j]
            sum = int((r + g + b) / 3)
            pix2[i, j] = sum

    gray.save(img.file.path.split('.')[0] + "_gray." + img.file.path.split('.')[1])
    im_grey_url = img.file.url.split('.')[0] + "_gray." + img.file.url.split('.')[1]

    # RED FILTER
    #
    cop = im.copy()
    w, h = cop.size
    pix = cop.load()
    for i in range(0, w):
        for j in range(0, h):
            r, g, b = pix[i, j]
            r = 255
            pix[i, j] = r, g, b
    cop.save(img.file.path.split('.')[0] + "_red." + img.file.path.split('.')[1])
    im_red_url = img.file.url.split('.')[0] + "_red." + img.file.url.split('.')[1]

    # GREEN FILTER
    #
    cop = im.copy()
    w, h = cop.size
    pix = cop.load()
    for i in range(0, w):
        for j in range(0, h):
            r, g, b = pix[i, j]
            g = 255
            pix[i, j] = r, g, b
    cop.save(img.file.path.split('.')[0] + "_green." + img.file.path.split('.')[1])
    im_green_url = img.file.url.split('.')[0] + "_green." + img.file.url.split('.')[1]

    # BLUE FILTER
    #
    cop = im.copy()
    w, h = cop.size
    pix = cop.load()
    for i in range(0, w):
        for j in range(0, h):
            r, g, b = pix[i, j]
            b = 255
            pix[i, j] = r, g, b
    cop.save(img.file.path.split('.')[0] + "_blue." + img.file.path.split('.')[1])
    im_blue_url = img.file.url.split('.')[0] + "_blue." + img.file.url.split('.')[1]

    # LUMINOSITY 1
    #
    cop = im.copy()
    pix = cop.load()
    w, h = cop.size
    for i in range(0, w):
        for j in range(0, h):
            r, g, b = pix[i, j]
            r = r/2
            g = g/2
            b = b/2
            pix[i, j] = r, g, b
    cop.save(img.file.path.split('.')[0] + "_lum1." + img.file.path.split('.')[1])
    im_lum1_url = img.file.url.split('.')[0] + "_lum1." + img.file.url.split('.')[1]

    # LUMINOSITY 2
    #
    cop = im.copy()
    pix = cop.load()
    w, h = cop.size
    for i in range(0, w):
        for j in range(0, h):
            r, g, b = pix[i, j]
            r = r * 2
            g = g * 2
            b = b * 2
            pix[i, j] = r, g, b
    cop.save(img.file.path.split('.')[0] + "_lum2." + img.file.path.split('.')[1])
    im_lum2_url = img.file.url.split('.')[0] + "_lum2." + img.file.url.split('.')[1]

    return render(request, 'compute_image.html', locals())
