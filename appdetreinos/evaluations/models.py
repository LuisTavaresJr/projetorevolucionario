from django.db import models

class Evaluation(models.Model):
    name = models.CharField('Nome', max_length=50)
    date = models.DateTimeField('avaliação criada em', auto_now_add=True)
    age = models.IntegerField('Idade')
    weight = models.FloatField('Peso')
    height = models.FloatField('Altura')
    bf = models.FloatField('BF')
    pathology = models.TextField('Patologia')
    objective = models.TextField('Objetivo')
    conditioning = models.TextField('Condicionamento Fisico')

    class Meta:
        verbose_name = 'avaliação'
        verbose_name_plural = 'avaliações'

    def __str__(self):
        return self.name