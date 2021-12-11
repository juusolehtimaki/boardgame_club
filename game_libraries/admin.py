from django.contrib import admin

# Register your models here.
from .models import Game, Loan

admin.site.register(Game)
admin.site.register(Loan)

