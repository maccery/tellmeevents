from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.generic import View
from django.template import RequestContext
import services


# Create your views here.
class CategoriesView(View):
    def get(self, request):
        categories = services.get_all_categories()['categories']

        return render_to_response('events/categories.html', {'categories': categories},
                                  context_instance=RequestContext(request))

class EventView(View):
    def get(self, request, events_id):
        event = services.get_event(events_id)

        return render_to_response('events/event.html', {'event': event})

class ResultsView(View):
    def get(self, request, page_number=1):
        category_ids = [request.GET.get('category1', ''), request.GET.get('category2', ''), request.GET.get('category3', '')]

        data = services.get_events(category_ids, page_number)
        page_count = data['pagination']['page_count']

        events = data['events']

        # Loop through the category ids we've been given and get the eventbrite object
        categories = []
        for category_id in category_ids:
            categories.append(services.get_category(category_id))

        return render_to_response('events/events.html', {'events': events, 'range': range(1, page_count), 'page_count': page_count, 'page_number': page_number, 'categories': categories},
                                  context_instance=RequestContext(request))
