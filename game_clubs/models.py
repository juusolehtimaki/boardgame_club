from django.db import models
from django.db.models.lookups import StartsWith
from django.contrib.auth.models import User
from django.forms.widgets import DateInput

# Create your models here.

class Game(models.Model):

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
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.my_review[:50]} --- {self.stars} stars."  

class GameInstance(models.Model):
    
    id = models.UUIDField(primary_key=True, default=())
    book = models.ForeignKey('Game', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and DateInput.today() > self.due_back:
            return True
        return False

    LOAN_STATUS = (
        ('d', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='d',
        help_text='Game availability')

    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set game as returned"),)

    def __str__(self):
        """String for representing the Model object."""
        return '{0} ({1})'.format(self.id, self.game.title)