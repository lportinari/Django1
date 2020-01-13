from django.shortcuts import render

# criando as minhas funções e retornando os meus templates


def index(request):
    print(dir(request.user))
    print(f"User: {request.user}")

    if str(request.user) == 'AnonymousUser':
        teste = 'Usuário não logado'
    else:
        teste = 'Usuário logado'

    context = {
        'curso': 'Programação Web com Django Fromework',
        'outro': 'Django é massa!',
        'logado': teste,
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
