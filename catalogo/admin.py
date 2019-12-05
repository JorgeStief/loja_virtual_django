from django.contrib import admin

from .models import Produto, Categoria, Imagem, Carrinho
# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','created','modified']
    search_fields = ['name','slug']
    list_filter = ['created', 'modified']
    
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug','category','created','modified']
    search_fields = ['name','slug','category__name']
    list_filter = ['created', 'modified']
    
class ImagemAdmin(admin.ModelAdmin):
    list_display = [ 'slug','product']
    #search_fields = ['name','slug','category__name']
    #list_filter = ['created', 'modified']


class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'produto','preco','quantidade','created','modified']
    search_fields = ['id']
    list_filter = ['created', 'modified']
        
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Produto,ProdutoAdmin)
admin.site.register(Imagem,ImagemAdmin)
admin.site.register(Carrinho,CarrinhoAdmin)

