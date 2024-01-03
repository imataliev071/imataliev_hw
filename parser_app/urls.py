from django.urls import path
from .views import ParserFormView

urlpatterns = [
    path('parser_film/', ParserFormView.as_view(), name='parser_film'),

]
