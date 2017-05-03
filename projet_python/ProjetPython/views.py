from django.shortcuts import render

# Create your views here.


def home(request):
    title = "Home"
    return render(request, "home.html", locals())


def galery(request):
    title = "Galery"
    return render(request, "galery.html", locals())


def upload(request):
    title = "Upload"
    return render(request, "upload.html", locals())
