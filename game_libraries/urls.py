from django.urls import path
from . import views

app_name = 'game_libraries'
urlpatterns = [
    path('', views.index, name='index'),
    path('games/', views.games, name='games'),
    path('games/<int:game_id>/', views.game, name='game'),
    path('new_game/', views.new_game, name='new_game'),
    path('new_loan/<int:game_id>/', views.new_loan, name='new_loan'),
    path('edit_loan/<int:loan_id>/', views.edit_loan, name='edit_loan'),
]