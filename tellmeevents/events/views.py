from django.shortcuts import render
from django.http import HttpResponse
import services

# Create your views here.
def index(request):
    categories = services.get_categories()
    return render(request, 'events/categories.html', categories)