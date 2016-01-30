from django.conf.urls import url
from . import views
from views import CategoriesView

urlpatterns = [
    url(r'^$', CategoriesView.as_view()),
]