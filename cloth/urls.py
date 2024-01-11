from django.urls import path
from . import views

urlpatterns = [
    path('all_cloth/', views.ProductList.as_view()),
    path('man_cloth/', views.ManClothView.as_view()),
    path('women_cloth/', views.WomenClothView.as_view()),
    path('child_cloth/', views.ChildClothView.as_view()),
    path('old_cloth/', views.OldClothView.as_view()),
]
