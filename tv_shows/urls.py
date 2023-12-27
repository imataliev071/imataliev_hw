from django.urls import path
from . import views

app_name = 'tv_shows'
urlpatterns = [
    path('', views.TvShowListView.as_view(), name='film_list'),
    path('film_list/<int:id>/', views.TvShowDetailView.as_view(), name='tv_shows_detail'),
    path('tv_shows_create/', views.TvShowCreateView.as_view(), name='tv_shows_create'),
    path('tv_shows_delete/', views.tv_shows_delete, name="tv_shows_list_delete"),
    path('tv_shows_drop/<int:id>/delete/', views.TvShowDropView.as_view(), name='tv_shows_drop'),
    path('tv_shows_list_update/', views.tv_shows_edit_view, name="tv_shows_list_update"),
    path('tv_shows_update/<int:id>/update/', views.TvShowUpdateView.as_view(), name="tv_shows_update"),
    path('search/', views.SearchView.as_view(), name='search')
]