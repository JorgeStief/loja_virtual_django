from django.contrib import admin

from .models import Produto, Categoria
# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','created','modified']
    search_fields = ['name','slug']
    list_filter = ['created', 'modified']
    
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','category','created','modified']
    search_fields = ['name','slug','category__name']
    list_filter = ['created', 'modified']
        
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Produto,ProdutoAdmin)