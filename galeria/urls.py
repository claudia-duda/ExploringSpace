from django.urls import path
from galeria.views import buscar, imagem

urlpatterns = [
    path('', buscar, name='buscar'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
]