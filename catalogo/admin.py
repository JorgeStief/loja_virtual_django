from django.contrib import admin

from .models import Produto, Categoria
# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','created','modified']
    search_fields = ['name','slug']
    
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','category','created','modified']
    search_fields = ['name','slug']
        
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Produto,ProdutoAdmin)