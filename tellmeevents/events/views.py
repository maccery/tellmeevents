from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.generic import View
from django.template import RequestContext
import services


# Create your views here.
class CategoriesView(View):
    def get(self, request):
        categories = services.get_categories()['categories']

        return render_to_response('events/categories.html', {'categories': categories}, context_instance=RequestContext(request))

    def post(self, request):
        category_ids = request.POST.getlist('categories[]')
        events = services.get_events(category_ids)['events']

        return render_to_response('events/events.html', {'events': events, 'category_ids': category_ids}, context_instance=RequestContext(request))
