from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import services


def index(request):
    categories = services.get_categories()
    return request, 'categories.html', categories
