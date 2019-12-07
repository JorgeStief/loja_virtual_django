from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings
# Create your models here.
import json
class Categoria(models.Model):
    name = models.CharField('Nome',max_length=100, default=None)
    slug = models.SlugField('Identificador',max_length=100, default=None,unique=True)
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

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Categoria.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)    


class Produto(models.Model):
    name = models.CharField('Nome', max_length=100,default=None)
    slug = models.SlugField('Identificador', max_length=100, default=None)
    category = models.ForeignKey('Categoria', verbose_name='Categoria',on_delete=models.CASCADE)
    description = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8, default=None)
    main_image = models.FileField('Imagem Principal', upload_to="images/", default=None)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField("Modificado em", auto_now_add=True)

    class Meta():
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']
        
    def get_absolute_path(self):
        return reverse('catalogo:produto_exibe', args=[self.category.slug, self.id, self.slug])
        
    def __str__(self):
        return self.name 

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Produto.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)           
    
class Imagem(models.Model):
    slug = models.FileField('Identificador', upload_to="images/", default=None)
    product = models.ForeignKey('Produto', verbose_name='Produto',on_delete=models.CASCADE)
    

    class Meta():
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'
        ordering = ['product']

class Carrinho(models.Model):

    produto = models.ForeignKey('Produto', verbose_name='Produto',on_delete=models.DO_NOTHING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='produtos',
                             on_delete=models.DO_NOTHING,
                             null=True)
    quantidade = models.IntegerField('Quantidade',default=0)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8, default=None)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField("Modificado em",auto_now_add=True)


    class Meta():
        verbose_name = 'Carrinho'
        verbose_name_plural = 'Carrinho'

        ordering = ['id']
        
    def get_absolute_path(self):
        return reverse('catalogo:produto_lista_por_categoria', args=[self.slug])

            