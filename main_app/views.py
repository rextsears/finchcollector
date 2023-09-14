from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch, Feeding
from .forms import FinchForm, FeedingForm

# Create your views here.

def finch_list(request):
    finches = Finch.objects.all()
    return render(request, 'finch_list.html', {'finches': finches})

def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finch_detail.html', {'finch': finch})

class FinchCreateView(CreateView):
    model = Finch
    form_class = FinchForm
    template_name = 'finch_create.html'
    success_url = '/finches/'

class FinchUpdateView(UpdateView):
    model = Finch
    form_class = FinchForm
    template_name = 'finch_edit.html'
    success_url = '/finches/'

class FinchDeleteView(DeleteView):
    model = Finch
    template_name = 'finch_confirm_delete.html'
    success_url = '/finches/'

def add_feeding(request, finch_id):
    finch = Finch.objects.get(pk=finch_id)
    feedings = Feeding.objects.filter(finch=finch)

    if request.method == 'POST':
        form = FeedingForm(request.POST)
        if form.is_valid():
            feeding = form.save(commit=False)
            feeding.finch = finch
            feeding.save()
            # Redirect to the same finch detail page after form submission
            return redirect('finch_detail', finch_id=finch_id)
    else:
        form = FeedingForm()

    return render(request, 'finch_detail.html', {'finch': finch, 'form': form, 'feedings': feedings})