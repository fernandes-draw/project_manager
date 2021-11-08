from django.contrib import admin
from .models import Produto, Codigo

# Register your models here.
admin.site.register(Produto)
admin.site.register(Codigo)