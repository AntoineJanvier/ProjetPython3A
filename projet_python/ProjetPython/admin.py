from django.contrib import admin
from .models import Image
# Register your models here.


class ImageAdmin(admin.ModelAdmin):
    resource_class = Image
    fields = ('name', 'file', 'style')
    list_display = ('name', 'file', 'style')
    search_fields = ('name', 'file', 'style')

admin.site.register(Image, ImageAdmin)
