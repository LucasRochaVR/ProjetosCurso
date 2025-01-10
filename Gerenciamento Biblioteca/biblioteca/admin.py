from django.contrib import admin
from .models import Livro, Usuario, Emprestimo

class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'genero', 'data_publicacao', 'isbn')
    search_fields = ('titulo', 'autor', 'isbn')
    list_filter = ('genero', 'data_publicacao')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'papel')
    search_fields = ('nome', 'email')
    list_filter = ('papel',)

class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('livro', 'usuario', 'data_emprestimo', 'status', 'data_devolucao')
    list_filter = ('status', 'data_emprestimo', 'data_devolucao')
    search_fields = ('livro__titulo', 'usuario__nome')

admin.site.register(Livro, LivroAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)
