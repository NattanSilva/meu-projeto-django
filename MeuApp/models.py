from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return f"<[{self.id}] - {self.nome} {self.sobrenome}, {self.idade}>"