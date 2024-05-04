from django.shortcuts import render
from django.shortcuts import redirect

from .models import Sugestion
# Create your views here.

def sugestion_list(request):
    sugestion = Sugestion.objects.all()
    return render(request, 'sugestion/pages/sugestion_list.html',
{'sugestion': sugestion})

def sugestion_detail(request, pk):
    sugestion = Sugestion.objects.get(pk=pk)
    return render(request, 'sugestion/pages/sugestion_detail.html',
{'sugestion': sugestion})


