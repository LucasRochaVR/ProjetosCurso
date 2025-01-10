from django.urls import path, include
from rest_framework import routers
from biblioteca.views import LivroViewSet,UsuarioViewSet,EmprestimoViewSet
from django.contrib import admin

router = routers.DefaultRouter()
router.register('livros', LivroViewSet, basename= 'livros' )
router.register('usuarios', UsuarioViewSet, basename= 'usuarios')
router.register('emprestimos', EmprestimoViewSet, basename= 'emprestimos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]