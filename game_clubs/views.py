from django.shortcuts import render,redirect
from .models import game, Review
from .forms import gameForm, ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    return render(request, 'game_clubs/index.html')

#@login_required
def games(request):

    games = game.objects.order_by('-date_added')
    context = { 'games': games }
    return render(request, 'game_clubs/games.html', context)

#@login_required
def reviews(request, game_id):

    game = game.objects.get(id=game_id)
    reviews = game.review_set.order_by('-date_added')
    context = {'game': game, 'reviews': reviews }
    return render(request, 'game_clubs/reviews.html', context)

@login_required
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
def new_review (request,game_id):
    game = game.objects.get(id=game_id)
    
    if request.method != 'POST':
        form =ReviewForm()
    else:
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.game = game
            new_review.save()
            return redirect('game_clubs:games', game_id=game_id)

    context = {'game':game, 'form':form}
    return render(request, 'game_clubs/new_review.html',context)


@login_required
def edit_game (request, game_id):

    game = game.objects.get(id=game_id)
    
    if request.method != 'POST':
        form = gameForm(instance=game)
    else:
        form = gameForm(instance=game, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('game_clubs:games', game_id=game_id)

    context = {'form':form, 'game': game}
    return render(request, 'game_clubs/edit_game.html',context)

@login_required
def edit_review(request, review_id):

    review = Review.objects.get(id=review_id)
    game = review.game
    
    if request.method != 'POST':
        form = gameForm(instance=review)
    else:
        form = gameForm(instance=review, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('game_clubs:game', game_id=game.id)

    context = {'review':review, 'game':game, 'form':form}
    return render(request, 'game_clubs/edit_review.html',context)

