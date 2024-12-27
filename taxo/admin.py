from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display =[
        'level',
        'description',
        'image',
        'answer'
    ]

@admin.register(models.Valid)
class AnswerAdmin(admin.ModelAdmin):
    list_display= [
        'user',
        'asked',
        'finish',
        'finished_at'
    ]

@admin.register(models.Useful)
class IdeaAdmin(admin.ModelAdmin):
    list_display=[
        'title',
        'idea',
        'back',
        'good'
    ]