from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Games
# Create your views here.
def index(request):
    games = Games.objects.all()
    return render(request, 'main/index.html', {'games': games})


def game_detail(request,game_slug):
    games = get_object_or_404(Games, slug=game_slug)
    return render(request, 'main/game.html', {'game': games})

def get_action(request):
    games = Games.objects.filter(genre='Action')
    return render(request, 'main/index.html', {'games': games})

def get_race(request):
    games = Games.objects.filter(genre='Race')
    return render(request, 'main/index.html', {'games': games})

def get_finance(request):
    games = Games.objects.filter(genre='Finance')
    return render(request, 'main/index.html', {'games': games})

def get_strategy(request):
    games = Games.objects.filter(genre='Strategy')
    return render(request, 'main/index.html', {'games': games})