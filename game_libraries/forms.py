from django import forms

from .models import Game, Loan

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['text']
        labels = {'text': ''}

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['text']
        labels = {'text' : 'Loan:' }
        widgets = {'text' : forms.Textarea(attrs={'cols':80})}