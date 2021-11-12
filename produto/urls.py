from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:produto_id>/', views.editar, name='editar'),
]
