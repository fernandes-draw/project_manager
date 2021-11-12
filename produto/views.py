from django.shortcuts import render, get_object_or_404
from .models import Produto


def index(request):
    produtos = Produto.objects.all()

    return render(request, 'produto/index.html', {'produtos': produtos})


def detalhe(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'produto/detalhe.html', {'produto': produto})
