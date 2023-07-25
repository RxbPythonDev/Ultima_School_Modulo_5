from django.db import models

# Modelo de Contato
class Contato(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)



# Modelo de Reserva
class Reserva(models.Model):
    nome_pet = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    data_reserva = models.DateField()
    observacoes = models.TextField()
