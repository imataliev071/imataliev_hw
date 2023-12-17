from django.urls import path
from . import views

urlpatterns = [
    path('film_list', views.tv_shows_list, name='film_list'),
    path('film_list/<int:id>/', views.tv_shows_detail , name='tv_shows_detail'),
]
