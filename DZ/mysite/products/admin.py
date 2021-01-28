from django.contrib import admin
from .models import Artiles

# Register your models here.

class ArtilesAdmin(admin.ModelAdmin):
    list_display= ('title', 'date','image','bit')
    
admin.site.register(Artiles, ArtilesAdmin)

# admin.site.register(Artiles)
