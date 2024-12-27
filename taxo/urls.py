from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = 'index'),
    path("Play/<int:user_id>", views.play, name ='play'),
    path('Options/', views.option, name = 'option'),
    path('About/', views.about, name= 'about'),
    path('question/<int:question_id>/', views.question, name = 'question'),
    path("Correct/<int:correct_id>/", views.correct, name = 'correct'),
    path('Answer/<int:answer_id>', views.answer, name= 'answer'),
    path('return/', views.indexed, name='indexed'),
    path('logins/', views.logins, name="logins"),
    path('logouts/', views.logouts, name="logouts"), 
    path("signup/", views.signup, name= "signup"),
]