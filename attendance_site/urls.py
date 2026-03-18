from django.urls import path

from calculator.views import home

urlpatterns = [
    path("", home, name="home"),
]
