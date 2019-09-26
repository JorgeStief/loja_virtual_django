from .models import Categoria

def Categorias(request):
    return {
        'categories': Categoria.objects.all()
    }