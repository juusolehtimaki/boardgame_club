from django.contrib import admin

# Register your models here.

from .models import Game, Review

admin.site.register(Game)
admin.site.register(Review)


