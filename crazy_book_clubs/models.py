from django.db import models
from django.db.models.lookups import StartsWith
from django.contrib.auth.models import User

# Create your models here.

class game(models.Model):

    name = models.CharField(max_length=200)
    authors = models.JSONField()
    year_published = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} by {','.join(self.authors)}."  


class Review(models.Model):

    my_review = models.TextField()
    stars = models.IntegerField()
    unfinished = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    game = models.ForeignKey(game, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.my_review[:50]} --- {self.stars} stars."  