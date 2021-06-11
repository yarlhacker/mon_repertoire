from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe



@admin.register(models.ListContact)
class ListContactAdmin(admin.ModelAdmin):
    list_display = ['view_image','nom','prenom','email','contact']

    def view_image(self,objet):
        return mark_safe(f'<img src = "{objet.photo.url}" width = 100px  height = 100px>')
    view_image.short_description = 'photo'    
    

    

# Register your models here.
