"""Defines URL patterns for the crazy_books_clubs application"""

from django.urls import path

from . import views

app_name = 'crazy_book_clubs'

urlpatterns = [
    path('', views.index, name="index"),
    path('games/', views.games, name='games'),
    path('games/<game_id>/', views.reviews, name='reviews'),
    path('new_game/', views.new_game, name='new_game'),
    path('new_review/', views.new_review, name='new_review'),
    path('edit_game/<int:game_id>/', views.edit_game, name='edit_game'),
    path('edit_review/<int:game_id>/', views.edit_review, name='edit_review')
]