from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Games
# Create your views here.
def index(request):
    games = Games.objects.all()
    return render(request, 'main/index.html', {'games': games})


def game_detail(request,game_slug):
    games = get_object_or_404(Games, slug=game_slug)
    return render(request, 'main/game.html', {'games': games})