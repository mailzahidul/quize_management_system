from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home" ),
    path('add_quiz/', views.add_quiz, name="add_quiz" ),
    path('quiz_test/', views.quiz_test, name="quiz_test" ),
    path('quiz_list/', views.quiz_list, name="quiz_list" ),
]
