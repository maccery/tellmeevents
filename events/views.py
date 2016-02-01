from django.shortcuts import render_to_response
from django.views.generic import View
from django.template import RequestContext
from services import Category, Event


class CategoriesView(View):
    def get(self, request):
        categories = Category().get_all_categories()

        return render_to_response('events/categories.html', {'categories': categories})


class EventView(View):
    def get(self, request, events_id):
        event = Event().get_event(events_id)

        return render_to_response('events/event.html', {'event': event})


class ResultsView(View):
    def get(self, request, page_number=1):
        category_ids = [request.GET.get('category1', ''), request.GET.get('category2', ''),
                        request.GET.get('category3', '')]

        data = Event().get_events(category_ids, page_number)
        categories = Category().get_categories(category_ids)
        events = data['events']
        total_pages = data['pagination']['page_count']

        return render_to_response('events/events.html',
                                  {'events': events, 'categories': categories,
                                   'range': range(1, total_pages),
                                   'page_count': total_pages,
                                   'page_number': page_number})
