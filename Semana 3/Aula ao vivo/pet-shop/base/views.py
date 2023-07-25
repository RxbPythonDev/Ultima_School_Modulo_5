from django.shortcuts import render
from base.forms import ContatoForm, ReservaForm

# View inicio, que é a primeira a ser acessada pelo usuário
def inicio(request):
    return render(request, 'inicio.html')



# View contato
def contato(request):
    # Definir sucesso, para indicar se o envio da mensagem foi correto ou não
    sucesso = False

    if request.method == 'GET': # Se for um método Get
        form = ContatoForm()
    # Se for um método POST
    else:
        form = ContatoForm(request.POST)
        if form.is_valid(): # Verificar se form é válido
            sucesso = True
            form.save()

    contexto = { # Definir o contexto da view contato
        'telefone': '(99) 99999.9999',
        'responsavel': 'Maria da Silva Pereira',
        'formulario': form ,
        'sucesso': sucesso
    }

    # Renderizar a página
    return render(request, 'contato.html', contexto)



# View para reserva de banho do pet
def reserva(request):
    # Sucesso no envio da mensagem
    sucesso = False
    
    if request.method == 'GET': # Se método da requisição é GET
        formulario = ReservaForm()
    # Método POST
    else:
        formulario = ReservaForm(request.POST)
        if formulario.is_valid(): # Verificar se form é válido
            sucesso = True
            formulario.save()

    contexto = { # Criar contexto da view de reserva
        'sucesso': sucesso,
        'formulario': formulario
    }

    return render(request, 'reserva.html', contexto)
