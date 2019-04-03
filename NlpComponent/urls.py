from django.urls import path

from .views import get_vector

urlpatterns = [
    path('get_vector/', get_vector),
]