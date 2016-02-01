from django.shortcuts import render_to_response
from django.views.generic import View
from services import Category, Event
from events.forms import SearchForm


class CategoriesView(View):
    def get(self, request):

        categories = Category().get_all_categories()

        if categories:
            form = SearchForm(categories)
            return render_to_response('events/categories.html', {'form': form})
        else:
            return render_to_response('events/no_categories_found.html')


class EventView(View):
    def get(self, request, events_id):
        event = Event().get_event(events_id)

        if event:
            return render_to_response('events/event.html', {'event': event})
        else:
            return render_to_response('events/no_event_found.html')


class ResultsView(View):
    def get(self, request, page_number=1):
        category_ids = [request.GET.get('category1', ''), request.GET.get('category2', ''),
                        request.GET.get('category3', '')]

        data = Event().get_events(category_ids, page_number)

        if data:
            events = data['events']
            page_count = data['pagination']['page_count']
            return render_to_response('events/events.html',
                                      {'events': events, 'range': range(1, 2), 'page_count': page_count})
        else:
            return render_to_response('events/no_results.html')
