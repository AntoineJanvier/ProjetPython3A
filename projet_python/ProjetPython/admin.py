from django.contrib import admin
from .models import Img
# Register your models here.


class ImgAdmin(admin.ModelAdmin):
    resource_class = Img
    fields = ('name', 'file')
    list_display = ('name', 'file')
    search_fields = ('name', 'file')

admin.site.register(Img, ImgAdmin)
