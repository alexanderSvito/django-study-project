from django.urls import path
from classes.views import TestView

urlpatterns = [
    path("test", TestView.as_view())
]
