from django.urls import path
from . import views

app_name = "w2v"
urlpatterns = [
    path("get_word_vector/", views.get_word_vector, name="get_word_vector"),
]