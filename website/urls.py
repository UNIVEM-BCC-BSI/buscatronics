from django.urls import path
from website.views.indexview import IndexView


urlpatterns = [
    path("categories/<int:id>", IndexView.as_view(), name="categories"),
    path("", IndexView.as_view(), name="index"),
]
