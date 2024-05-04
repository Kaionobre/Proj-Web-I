from django.urls import path
from . import views

# import up  here

urlpatterns = [
 path('', views.sugestion_list, name='sugestion_list'),
 path('sugestion/<int:pk>/', views.sugestion_detail, name='sugestion_detail'),
]