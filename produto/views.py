from django.shortcuts import render
from .models import Produto


# Create your views here.
def index(request):
    produtos = Produto.objects.all()

    context = {
        'produtos': produtos,
    }

    return render(request, 'produto/index.html', context=context)
