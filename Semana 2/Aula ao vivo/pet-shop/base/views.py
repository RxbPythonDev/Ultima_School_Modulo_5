from django.shortcuts import render
from base.forms import ContatoForm, ReservaForm

# Create your views here.
# Definir uma view inicial


def inicio(request):
    return render(request, 'inicio.html')


# View de contatos
def contato(request):
    sucesso = False
    if request.method == 'GET':
        form = ContatoForm()
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():
            sucesso = True

    contexto = {
        'telefone': '(99)99999.9999',
        'responsavel': 'Maria da Silva Pereira',
        'formulario': form,
        'sucesso': sucesso
    }

    return render(request, 'contato.html', contexto)

def reserva(request):
    sucesso = False
    if request.method == 'GET':
        formulario = ReservaForm()
    else:
        formulario = ReservaForm(request.POST)
        if formulario.is_valid():
            sucesso = True
    contexto = {
        'sucesso': sucesso,
        'formulario': formulario
    }
    return render(request, 'reserva.html', contexto)