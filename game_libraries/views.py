from django.shortcuts import render, redirect
from .models import Game
from .forms import GameForm
# Create your views here.
def index(request):
    return render(request, 'game_libraries/index.html')
    
def games(request):
    games=Game.objects.order_by('date_added')
    context = {'games':games}
    return render(request, 'game_libraries/games.html', context)

def game(request, game_id):
    game = Game.objects.get(id=game_id)
    loans = game.loan_set.order_by('-date_added')
    context = {'game':game, 'loans':loans}
    return render(request, 'game_libraries/game.html', context)

def new_game(request):
    if request.method != 'POST':
        form = GameForm()
    else:
        form = GameForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('game_libraries:games')
    context = {'form' : form}
    return render(request, 'game_libraries/new_game.html', context)


