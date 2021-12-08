"""Defines URL patterns for the crazy_books_clubs application"""

from django.urls import path

from . import views

app_name = 'game_clubs'

urlpatterns = [
    path('', views.index, name="index"),
    path('games/', views.games, name='games'),
    
    path('new_game/', views.new_game, name='new_game'),
    
    path('edit_game/<int:game_id>/', views.edit_game, name='edit_game'),
    
]