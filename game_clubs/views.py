from django.shortcuts import render,redirect


from .models import Game, Review
from .forms import gameForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    
    return render(request, 'game_clubs/index.html')
    

#@login_required
def games(request):

    games = Game.objects.order_by('-date_added')
    context = { 'games': games }
    return render(request, 'game_clubs/games.html', context)

#@login_required
def game(request):

    game = Game.objects.order_by('-date_added')
    context = {'game': game}
    return render(request, 'game_clubs/game.html', context)




#@login_required
def new_game (request):
    
    if request.method != 'POST':
        form =gameForm()
    else:
        form = gameForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('game_clubs:games')

    context = {'form':form}
    return render(request, 'game_clubs/new_game.html',context)


@login_required
def edit_game (request, game_id):

    game = games.objects.get(id=game_id)
    game = Review.game
    
    if request.method != 'POST':
        form = gameForm(instance=game)
    else:
        form = gameForm(instance=game, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('game_clubs:games', game_id=game_id)

    context = {'form':form, 'game': game}
    return render(request, 'game_clubs/edit_game.html',context)



