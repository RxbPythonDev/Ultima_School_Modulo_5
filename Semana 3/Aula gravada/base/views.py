from django.shortcuts import render

from base.forms import InscreverForm

from base.models import Contato

from eventos.models import Categoria


def inicio(request):
    dados = []
    dados.append(
        {
            'titulo': 'Titulo Legal 1',
            'categoria': 'Categoria 1',
            'data': '30/08/2022',
        }
    )
    dados.append(
        {
            'titulo': 'Titulo Legal 2',
            'categoria': 'Categoria 2',
            'data': '29/08/2022',
        },
    )
    contexto = {
        'dados': dados,
    }
    resposta = render(request, 'inicio.html', contexto)
    return resposta


def inscrever(request):
    contexto = {'sucesso': False}
    form = InscreverForm(request.POST or None)
    if form.is_valid():
        form.save()
        contexto['sucesso'] = True
    contexto['form'] = form
    return render(request, 'inscrever.html', contexto)
