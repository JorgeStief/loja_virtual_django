from django.db import models
from django.urls import reverse

# Create your models here.

class Categoria(models.Model):
    name = models.CharField('Nome',max_length=100, default=None)
    slug = models.SlugField('Identificador',max_length=100, default=None)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField("Modificado em",auto_now_add=True)

    class Meta():
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']
        
    def get_absolute_path(self):
        return reverse('catalogo:produto_lista_por_categoria', args=[self.slug])
    def __str__(self):
        return self.name 


class Produto(models.Model):
    name = models.CharField('Nome', max_length=100,default=None)
    slug = models.SlugField('Identificador', max_length=100, default=None)
    category = models.ForeignKey('Categoria', verbose_name='Categoria',on_delete=models.CASCADE)
    description = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8, default=None)
    main_image = models.CharField('Imagem Principal', max_length=200, default=None)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField("Modificado em", auto_now_add=True)

    class Meta():
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']
        
    def get_absolute_path(self):
        return reverse('catalogo:produto_exibe', args=[self.id, self.slug])
        
    def __str__(self):
        return self.name    
    
class Imagem(models.Model):
    slug = models.SlugField('Identificador', max_length=300, default=None)
    product = models.ForeignKey('Produto', verbose_name='Produto',on_delete=models.CASCADE)
    

    class Meta():
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'
        ordering = ['product']
            