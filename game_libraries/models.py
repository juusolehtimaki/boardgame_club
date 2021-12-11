from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game (models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text

class Loan(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'loans'

    def __str__(self):
        return f"{self.text[50]}..."