from django.shortcuts import render
from .models import Finch

# Create your views here.

def finch_list(request):
    finches = Finch.objects.all()
    return render(request, 'finch_list.html', {'finches': finches})

def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finch_detail.html', {'finch': finch})
