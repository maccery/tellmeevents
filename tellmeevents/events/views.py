from django.shortcuts import render_to_response
from django.http import HttpResponse
import services


# Create your views here.
def index(request):
    categories = services.get_categories()['categories']

    return render_to_response('events/categories.html', {'categories': categories})


def events(request):
    category_ids = [108]
    events = services.get_events(category_ids)['events']

    return render_to_response('events/events.html', {'events': events})
