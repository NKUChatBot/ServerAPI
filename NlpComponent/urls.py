from django.urls import path

from .views import get_vector, ask

urlpatterns = [
    path('get_vector/', get_vector),
    path('ask/', ask),
]