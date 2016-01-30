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


class ResultsView(View):
    def post(self, request):
        category_ids = request.POST.getlist('categories[]')

        data = services.get_events(category_ids, 1)
        page_count = data['pagination']['page_count']
        page_number = data['pagination']['page_number']

        events = data['events']

        # Loop through the category ids we've been given and get the eventbrite object
        categories = []
        for category_id in category_ids:
            categories.append(services.get_category(category_id))

        return render_to_response('events/events.html', {'events': events, 'range': range(1, page_count), 'page_count': page_count, 'page_number': page_number, 'categories': categories},
                                  context_instance=RequestContext(request))
