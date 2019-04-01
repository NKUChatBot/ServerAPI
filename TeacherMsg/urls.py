from django.urls import path, include

from .views import ask

urlpatterns = [
    path('ask/', ask),
]