from django import forms

from base.models import Reserva

class ContatoForm(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
            'nome_pet',
            'telefone',
            'dia_reserva',
            'observacoes'
        ]