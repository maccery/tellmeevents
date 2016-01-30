from django.conf.urls import url
from . import views
from views import CategoriesView, ResultsView, EventView

urlpatterns = [
    url(r'^$', CategoriesView.as_view()),
    url(r'^results$', ResultsView.as_view(), name='events_search'),
    url(r'^results/(?P<page_number>\w+)/$', ResultsView.as_view()),
    url(r'^event/(?P<events_id>\w+)/$', EventView.as_view()),
]