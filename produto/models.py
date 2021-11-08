from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=150)
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome + " - " + str(self.data_cadastro)

class Codigo(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=10)

    def __str__(self):
        return self.codigo + " - " + str(Produto.objects.get())
    