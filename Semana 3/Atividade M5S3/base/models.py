from django.db import models

# Create your models here.
class Reserva(models.Model):
    nome_pet = models.CharField('Nome do Pet', max_length=50)
    telefone = models.CharField(max_length=11)
    dia_reserva = models.DateField('Dia da reserva')
    observacoes = models.TextField('Observações',blank=True)