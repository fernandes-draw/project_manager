from django.db import models

# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    image = models.ImageField(upload_to='produto/images/')
    data_cadastro = models.DateField(auto_now=True)
    codigo_01 = models.CharField(max_length=10)
    codigo_02 = models.CharField(max_length=10, null=True, default="-")
    codigo_03 = models.CharField(max_length=10, null=True, default="-")

    def __str__(self):
        return self.nome + " - " + self.codigo_01 + " - " + self.codigo_02 + " - " + self.codigo_03
