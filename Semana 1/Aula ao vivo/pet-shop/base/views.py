from django.shortcuts import render

# Create your views here.
# Definir uma view inicial
def inicio(request):
    return render(request, 'inicio.html')


# View de contatos
def contato(request):
    return render(request, 'contato.html')