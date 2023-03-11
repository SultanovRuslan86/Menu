from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Category, Product

def index(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'appmenu/index.html', context)