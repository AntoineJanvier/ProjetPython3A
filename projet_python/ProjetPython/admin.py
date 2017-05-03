from django.contrib import admin
from .models import Img
# Register your models here.


class ImgAdmin(admin.ModelAdmin):
    resource_class = Img
    fields = ('name', 'file', 'style')
    list_display = ('name', 'file', 'style')
    search_fields = ('name', 'file', 'style')

admin.site.register(Img, ImgAdmin)
