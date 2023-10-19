from django.db import models

class Instituicao(models.Model):
    nome = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    site = models.URLField()

    def __str__(self):
        return self.nome