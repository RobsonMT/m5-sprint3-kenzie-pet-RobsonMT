from django.urls import path
from animals.views import AnimalView

urlpatterns = [
    path("animals/", AnimalView.as_view()),
]
