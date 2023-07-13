from django.shortcuts import render

from base.forms import InscreverForm

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
        'dados': dados
    }
    resposta = render(request, 'inicio.html', contexto)
    return resposta

def inscrever(request):
    contexto = {'sucesso': False}
    form = InscreverForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data['nome'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['observacao'])
        print(form.cleaned_data['data'])
        contexto['sucesso'] = True
    contexto['form'] = form
    return render(request, 'inscrever.html', contexto)