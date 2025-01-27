from django.urls import path
from  apps.galeria.views import buscar, deletar_imagem, editar_imagem, imagem, nova_imagem

urlpatterns = [
    path('', buscar, name='buscar'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('nova-imagem', nova_imagem, name='nova-imagem'),
    path('editar-imagem/<int:foto_id>', editar_imagem, name='editar-imagem'),
    path('deletar-imagem/<int:foto_id>',deletar_imagem, name='deletar-imagem'),
]