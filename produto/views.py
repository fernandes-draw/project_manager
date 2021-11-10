from django.shortcuts import render
from .models import Produto, Codigo


# Create your views here.
def index(request):
    produtos = Produto.objects.all()
    codigos = Codigo.objects.all()
    lista = []
    for codigo in codigos:
        lista.append(codigo)

    context = {
        'produtos': produtos,
        'codigos': lista
    }

    return render(request, 'produto/index.html', context=context)
