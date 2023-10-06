from django.urls import path
from . import views

urlpatterns = [
    path('story/', views.story, name='story'),
    path('home/', views.learn, name='learn'),
]
