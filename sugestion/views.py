from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from django.urls import reverse_lazy
from .models import Sugestion

# Create your views here.

class SugestionCreateView(CreateView):
    model = Sugestion
    fields = ['nome', 'descricao', 'image']
    template_name = 'sugestion/pages/sugestion_create.html'
    success_url = '/sugestion'

class SugestionDetailView(DetailView):
    model = Sugestion
    template_name = 'sugestion/pages/sugestion_detail.html'

class SugestionUpdateView(UpdateView):
    model = Sugestion
    fields = ['nome', 'descricao', 'image']
    template_name = 'sugestion/pages/sugestion_edit.html'
    success_url = '/sugestion'

class SugestionDeleteView(DeleteView):
    model = Sugestion
    template_name = 'sugestion/pages/sugestion_delete.html'
    success_url = reverse_lazy('sugestion_list')

class SugestionListView(ListView):
    model = Sugestion
    template_name = 'sugestion/pages/sugestion_list.html'
    context_object_name = 'sugestion'






