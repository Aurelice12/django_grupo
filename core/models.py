from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Categoria(models.Model): 
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.ManyToManyField(Autor)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    usuario = models.ManyToManyField(Usuario)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True) 

    def __str__(self):
        return self.titulo

class Emprestimo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(max_length=100, null=True)
    data_devolucao = models.DateField(max_length=100, null=True)

    def __str__(self):
        return f'{self.usuario.username} - {self.livro.titulo}'
