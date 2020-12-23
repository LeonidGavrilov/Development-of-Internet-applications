from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.

def products_home(request):
    products = Artiles.objects.order_by('-date')
    return render(request, 'products/products_home.html', {'products':products})

class NewDetailView(DetailView):
    model = Artiles
    template_name = 'products/details_view.html'
    context_object_name = 'article'

class NewUpdateView(UpdateView):
    model = Artiles
    template_name = 'products/create.html'
    form_class = ArtilesForm
    # fields = ['title','anons','full_text','date']

class NewDeleteView(DeleteView):
    model = Artiles
    success_url = '/products'
    template_name = 'products/news-delete.html'
    # fields = ['title','anons','full_text','date']

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = ArtilesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'products/create.html', data)