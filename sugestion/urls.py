from django.urls import path
from . import views
from .views import SugestionCreateView, SugestionDetailView, SugestionUpdateView, SugestionDeleteView, SugestionListView
# import up  here

urlpatterns = [
 path('', SugestionListView.as_view(), name='sugestion_list'), 
 path('create/', SugestionCreateView.as_view(), name='sugestion_create'), 
 path('<int:pk>/', SugestionDetailView.as_view(), name='sugestion_detail'), 
 path('<int:pk>/edit/', SugestionUpdateView.as_view(), name='sugestion_edit'), 
 path('<int:pk>/delete/', SugestionDeleteView.as_view(), name='sugestion_delete'),
]