from django.shortcuts import render

# criando as minhas funções e retornando os meus templates


def index(request):
    context = {
        'curso': 'Programação Web com Django Fromework'
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
