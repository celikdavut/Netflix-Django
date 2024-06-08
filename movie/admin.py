from django.contrib import admin
from .models import *

class MoviesAdmin(admin.ModelAdmin):
    list_display=["id","isim","kategori"]
    list_display_links=["id"]
    list_editable=["isim"]
    list_filter=["kategori"]
    list_per_page=2
    
# Register your models here.

admin.site.register(Movies,MoviesAdmin)
admin.site.register(Kategoriler)