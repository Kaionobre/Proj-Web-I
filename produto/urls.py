from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categoria/<str:categoria>/', views.categoria, name='categoria'),
]
