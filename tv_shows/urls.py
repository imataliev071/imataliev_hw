from django.urls import path
from . import views

urlpatterns = [
    path('', views.tv_shows_list, name='film_list'),
    path('film_list/<int:id>/', views.tv_shows_detail, name='tv_shows_detail'),
    path('tv_shows_create/', views.tv_shows_create, name='tv_shows_create'),
    path('tv_shows_delete/', views.tv_shows_delete, name="tv_shows_list_delite"),
    path('tv_shows_drop/<int:id>/delete/', views.tv_drop_view, name='tv_shows_drop'),
    path('tv_shows_list_update/', views.tv_shows_edit_view, name="tv_shows_list_update"),
    path('tv_shows_update/<int:id>/update/', views.tv_shows_update, name="tv_shows_update"),

]