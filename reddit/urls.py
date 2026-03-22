from django.urls import path
from . import views

urlpatterns = [
    path('', views.reddit_list, name='reddit_list'),
    path('create/', views.reddit_create, name='reddit_create'),

    path('<int:reddit_id>/edit/', views.reddit_edit, name='reddit_edit'),
    path('<int:reddit_id>/delete/', views.reddit_delete, name='reddit_delete'),
    path('register/', views.register, name='register'),

] 
