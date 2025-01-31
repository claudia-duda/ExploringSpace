from django.urls import include, path
from  apps.galeria.views import buscar, deletar_imagem, editar_imagem, imagem, nova_imagem
from rest_framework import routers
from apps.galeria.views import FotografiaViewSet

router = routers.DefaultRouter()
router.register('fotografias', FotografiaViewSet, basename= 'fotografias')



urlpatterns = [
    path('api/', include(router.urls)),
    path('', buscar, name='buscar'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('nova-imagem', nova_imagem, name='nova-imagem'),
    path('editar-imagem/<int:foto_id>', editar_imagem, name='editar-imagem'),
    path('deletar-imagem/<int:foto_id>',deletar_imagem, name='deletar-imagem'),
]