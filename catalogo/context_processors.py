from .models import Categoria
from datetime import date



def Categorias(request):
    return {
        'categorias': Categoria.objects.all()
    }

def Data(request):
    data_atual = date.today()
    #data_em_texto = ‘{}/{}/{}’.format(data_atual.day, data_atual.month,data_atual.year)
    return {
        'data': data_atual
    }
