from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .models import Img
from PIL import Image
from . import image_process
from django.conf import settings


def home(request):
    title = "Home"
    images = Img.objects.all()
    return render(request, "home.html", locals())


def upload(request):
    title = "Upload"
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'upload.html', locals())
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', locals())


def compute_image(request, id):
    if request.method == 'POST':
        seuil = int(request.POST['seuil'])
    else:
        seuil = 150
    
    title = "Compute image"
    img = Img.objects.get(id=id)
    im = Image.open(img.file.path)

    im_inverted_url = image_process.img_proc(img, im, seuil, "INVERTED")
    im_grey_url = image_process.img_proc(img, im, seuil, "GREY")
    im_red_url = image_process.img_proc(img, im, seuil, "RED")
    im_green_url = image_process.img_proc(img, im, seuil, "GREEN")
    im_blue_url = image_process.img_proc(img, im, seuil, "BLUE")
    im_lum1_url = image_process.img_proc(img, im, seuil, "LUM1")
    im_lum2_url = image_process.img_proc(img, im, seuil, "LUM2")
    im_vertsym_url = image_process.img_proc(img, im, seuil, "VERTICAL_SYMMETRY")
    im_fillred_url = image_process.img_proc(img, im, seuil, "FILL_RED")
    im_fillgreen_url = image_process.img_proc(img, im, seuil, "FILL_GREEN")
    im_fillblue_url = image_process.img_proc(img, im, seuil, "FILL_BLUE")

    return render(request, 'compute_image.html', locals())
