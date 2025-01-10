from rest_framework import viewsets
from .models import Livro, Usuario, Emprestimo
from .serializers import LivroSerializer, UsuarioSerializer, EmprestimoSerializer
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

class LivroViewSet(viewsets.ModelViewSet):
    authenthication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo', 'autor']

class UsuarioViewSet(viewsets.ModelViewSet):
    authenthication_classes = [BasicAuthentication]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    search_fields = ['nome']
    permission_classes = [IsAuthenticated]

class EmprestimoViewSet(viewsets.ModelViewSet):
    authenthication_classes = [BasicAuthentication]
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    permission_classes = [IsAuthenticated]
