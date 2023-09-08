from django.shortcuts import render
from django.views.generic import ListView,DetailView

from django.views.generic.edit import CreateView

from .models import Menu,Book
# from .forms import Productform 



def home(request):
    template_name='litlelemonresturant/home.html'
    context={}
    return render(request, template_name, context)


def about(request):
    template_name='litlelemonresturant/about.html'
    context={}
    return render(request, template_name, context)

class PostListView(ListView):
    model = Menu
    template_name="litlelemonresturant/Menu.html"
    context_object_name="posts"

class PostDetailView(DetailView):
    model = Menu
    context_object_name="posts"
    
    
# ======================== this is booking meal class ===========
class BookMeal(CreateView):
 
    # specify the model for create view
    model = Book
    template_name="litlelemonresturant/Book.html"
 
    # specify the fields to be displayed
 
    fields = ['Name', 'Price','Description','phone_number']

# def Menu(request):
#     template_name='Menu.html'
#     context={}
#     return render(request, template_name, context)


# def Book(request):
#     template_name='Book.html'
#     context={}
#     return render(request, template_name, context)

