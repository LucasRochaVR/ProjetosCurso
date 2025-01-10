from django.db import models

class Usuario(models.Model):
    ADMIN = 'admin'
    LEITOR = 'leitor'
    PAPEL_CHOICES = [
        (ADMIN, 'Administrador'),
        (LEITOR, 'Leitor'),
    ]
    
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    papel = models.CharField(max_length=6, choices=PAPEL_CHOICES, default=LEITOR)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    genero = models.CharField(max_length=100)
    data_publicacao = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo

class Emprestimo(models.Model):
    PENDENTE = 'pendente'
    EMPRESTADO = 'emprestado'
    DEVOLVIDO = 'devolvido'
    STATUS_CHOICES = [
        (PENDENTE, 'Pendente'),
        (EMPRESTADO, 'Emprestado'),
        (DEVOLVIDO, 'Devolvido'),
    ]
    
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDENTE)

    def __str__(self):
        return f"{self.livro.titulo} - {self.usuario.nome} ({self.status})"
