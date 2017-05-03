from django.contrib import admin
from .models import Image
# Register your models here.


class ImageAdmin(admin.ModelAdmin):
    resource_class = Image
    fields = ('name', 'path', 'style')
    list_display = ('name', 'path', 'style')
    search_fields = ('name', 'path', 'style')

admin.site.register(Image, ImageAdmin)
