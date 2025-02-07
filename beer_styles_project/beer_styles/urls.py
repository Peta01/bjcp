from django.urls import path
from . import views

urlpatterns = [
    path('', views.beer_style_list, name='beer_style_list'),
    path('<int:pk>/', views.beer_style_detail, name='beer_style_detail'),
]
