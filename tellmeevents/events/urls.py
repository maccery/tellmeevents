from django.conf.urls import url
from . import views
from views import CategoriesView, ResultsView

urlpatterns = [
    url(r'^$', CategoriesView.as_view()),
    url(r'^results$', ResultsView.as_view()),
    url(r'^results/(?P<page_number>\w+)/$', ResultsView.as_view())
]