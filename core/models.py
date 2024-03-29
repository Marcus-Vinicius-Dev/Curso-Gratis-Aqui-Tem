from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    email = models.EmailField(
        max_length=50,
        null=False,
        blank=False
    )
    

class Instituicao(models.Model):
    #cnpj = models.CharField(
    #    max_length = 18,
    #    null = False,
    #    blank = False
    #)
    
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cep = models.CharField(
        max_length=9,
        null=False,
        blank=False
    )
    
    endereco = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cidade = models.CharField(
        max_length=150,
        null=True,
        blank=True
    )
    
    uf = models.CharField(
        max_length=2,
        null=False,
        blank=False
    )

    telefone = models.CharField(
        max_length=15,
        null=False,
        blank=False
    )
    
    email = models.EmailField(
        max_length=50,
        null=True,
        blank=True
    )
    
    site = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    
    objetos = models.Manager()

    def __str__(self):
        return f"{self.nome}"



class Cursos(models.Model):
    

    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)

    nome = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    descricao = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    CATEGORIAS_CHOICES = [
        ('culinaria', 'Culinária'),
        ('danca', 'Dança'),
        ('esportes', 'Esportes'),
        ('idiomas', 'Idiomas'),
        ('musica', 'Música'),
        ('negocios', 'Negócios'),
        ('tecnologia', 'Tecnologia'),
        ('artes', 'Artes'),
        ('outros', 'Outros'),
        # Adicione quantas categorias você desejar
    ]

    categoria = models.CharField(
        max_length=50,
        choices=CATEGORIAS_CHOICES,
        default='categoria1'  # Categoria padrão
    )
    
    inscricao = models.DateField(
        null=True,
        blank=True
    )
    data_de_criacao = models.DateTimeField(auto_now_add=True) 
    
    objetos = models.Manager()

    def __str__(self):
        return f"{self.nome} [R$ {self.descricao}]"
    

#class Categorias(models.Model):
#    nome = models.CharField(
#        max_length=100,
#        null=False,
#        blank=False
#    )

#    descricao = models.CharField(
#        max_length=255,
#        null=False,
#        blank=False
#    )


#    objetos = models.Manager()

#    def __str__(self):
#        return f"{self.nome} [R$ {self.descricao}]"
    
class Estudante(models.Model):
    nome=models.CharField(max_length=100)
    sobrenome=models.CharField(max_length=100)
    data_nascimento=models.DateField()
    telefone=models.CharField(max_length = 15)
    #celular = models.CharField(max_length = 15)
    email=models.EmailField()
    sexo=models.CharField(max_length=1)

    def __str__(self):
        return self.nome



