from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=100)
    periodoIngresso = models.CharField('Período Ingresso', max_length=10)
    nota = models.DecimalField('Nota',decimal_places=2,max_digits=8)
    situacao= models.CharField('Situação', max_length=50)

    def __str__(self):
        return f'{self.nome}'

class AlunoInfo(models.Model):
    nome = models.CharField('Nome', max_length=100)
    periodoIngresso = models.CharField('Período Ingresso', max_length=10)
    nota = models.DecimalField('Nota',decimal_places=2,max_digits=8)
    situaacao= models.CharField('Situação', max_length=50)