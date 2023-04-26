from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id','nombre']
    list_display = ['id','nombre']

# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor)
admin.site.register(Post)
