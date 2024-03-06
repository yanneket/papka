from django.http import HttpResponse
from django.shortcuts import render

context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        'text_on_page': 'Любой текст о магазине'
    }

def index(request):
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html', context)
