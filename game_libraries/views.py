from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Game, Loan
from .forms import GameForm, LoanForm
from django.http import Http404


# Create your views here.
def index(request):
    return render(request, 'game_libraries/index.html')

@login_required   
def games(request):
    """Show all games"""
    games=Game.objects.order_by('date_added')
    context = {'games':games}
    return render(request, 'game_libraries/games.html', context)

@login_required 
def game(request, game_id):
    game = Game.objects.get(id=game_id)
    # Make sure the game belongs to the current user
    
    loans = game.loan_set.order_by('-date_added')
    context = {'game':game, 'loans':loans}
    return render(request, 'game_libraries/game.html', context)

@login_required  
def new_game(request):
    if request.method != 'POST':
        form = GameForm()
    else:
        form = GameForm(data=request.POST)
        if form.is_valid():
            new_game = form.save(commit=False)
            new_game.owner = request.user
            new_game.save()
            return redirect('game_libraries:games')
    context = {'form' : form}
    return render(request, 'game_libraries/new_game.html', context)

@login_required  
def new_loan(request, game_id):
    game = Game.objects.get(id=game_id)

    if request.method != 'POST':
        form = LoanForm()
    else:
        form = LoanForm(data=request.POST)
        if form.is_valid():
            new_loan = form.save(commit=False)
            new_loan.game = game
            new_loan.save()
            return redirect('game_libraries:game', game_id=game_id)

    context = {'game': game, 'form': form }
    return render(request, 'game_libraries/new_loan.html', context)

@login_required  
def edit_loan(request, loan_id):
    loan = Loan.objects.get(id=loan_id)
    game = loan.game
    if game.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = LoanForm(instance=loan)
    else:
        form = LoanForm(instance=loan, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('game_libraries:game', game_id=game.id)
    context = {'loan':loan, 'game':game, 'form':form}
    return render(request, 'game_libraries/edit_loan.html', context)




