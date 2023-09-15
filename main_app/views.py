from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch, Feeding, Toy
from .forms import FinchForm, FeedingForm, ToyForm

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
    form = FeedingForm(request.POST)
    if form.is_valid():
        feeding = form.save(commit=False)
        feeding.finch = finch
        feeding.save()
        return redirect('finch_detail', finch_id=finch_id)
    else:
        form = FeedingForm()

    return render(request, 'finch_detail.html', {'finch': finch, 'form': form})

class ToyCreateView(CreateView):
    model = Toy
    form_class = ToyForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['finch_id'] = self.kwargs['finch_id']
        return context

    def form_valid(self, form):
        form.instance.finch_id = self.kwargs['finch_id']
        return super().form_valid(form)

    def get_success_url(self):
        finch_id = self.kwargs.get('finch_id')
        if finch_id is not None:
            return reverse('finch_detail', args=[finch_id])
    
def add_toy(request, finch_id):
    finch = Finch.objects.get(pk=finch_id)

    if request.method == 'POST':
        form = ToyForm(request.POST)
        if form.is_valid():
            toy = form.save(commit=False)
            toy.finch = finch
            toy.save()
            return redirect('finch_detail', finch_id=finch_id)
    else:
        form = ToyForm()

    return render(request, 'add_toy.html', {'finch': finch, 'form': form})