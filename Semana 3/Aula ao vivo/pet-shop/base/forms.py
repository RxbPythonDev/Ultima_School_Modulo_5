from django import forms
from base.models import Contato, Reserva

# Formulario contato
class ContatoForm(forms.ModelForm):
    class Meta:
        # Definir o modelo base
        model = Contato
        # Definir os campos
        fields = ['nome', 'email', 'mensagem']

        # Definir os widgets
        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'placeholder': 'Insira seu nome aqui'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Insira seu e-mail aqui'
                }
            ),
            'mensagem': forms.Textarea(
                attrs={
                    'placeholder': 'Insira sua mensagem aqui'
                }
            )
        }

        # Definir as labels do campo
        labels = {
            'nome': 'Nome:',
            'email': 'E-mail:',
            'mensagem': 'Mensagem:'
        }



# Data com calendário
class DateInput(forms.DateInput):
    input_type = 'date'



# Formulário de reserva
class ReservaForm(forms.ModelForm):
    class Meta:
        # Definir o modelo base
        model = Reserva
        # Definir os campos
        fields = ['nome_pet', 'telefone', 'data_reserva', 'observacoes']

        # Definir os widgets
        widgets = {
            'nome_pet': forms.TextInput(
                attrs={
                    'placeholder': 'Insira o nome do seu pet aqui'
                }
            ),
            'telefone': forms.TextInput(
                attrs={
                    'placeholder': 'Insira seu telefone aqui'
                }
            ),
            'data_reserva': DateInput(),
            'observacoes': forms.TextInput(
                attrs={
                    'placeholder': 'Insira suas observações aqui'
                }
            )
        }

        # Definir as labels do campos
        labels = {
            'nome_pet': 'Nome do Pet:',
            'telefone': 'Telefone:',
            'data_reserva': 'Data de Reserva do Banho:',
            'observacoes': 'Observações'
        }
