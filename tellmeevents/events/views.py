from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import services

# Create your views here.
def index(request):
    categories = services.get_categories()['events']
    return render_to_response('events/categories.html', {'categories': categories})