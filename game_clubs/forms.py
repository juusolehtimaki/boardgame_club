from django import forms
from .models import game, Review

class gameForm(forms.ModelForm):
    class Meta:
        model = game
        fields = ['name','authors','year_published']
        labels = {'name':'', 'authors':'','year_published':''}
        

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['my_review','stars','unfinished']
        labels = {'my_review': '','stars':'','unfinished':''}
        