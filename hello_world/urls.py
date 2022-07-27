from django.urls import path

from hello_world.views import hello

urlpatterns = [
    path('', hello)
]