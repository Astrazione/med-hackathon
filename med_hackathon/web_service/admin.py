from django.contrib import admin

# Register your models here.
from .models import Subject, Chapter, Theme



admin.site.register(Subject)
admin.site.register(Chapter)
admin.site.register(Theme)