from django.contrib import admin

# Register your models here.

from .models import game, Review

admin.site.register(game)
admin.site.register(Review)


