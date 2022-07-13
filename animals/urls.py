from django.urls import path
from animals.views import AnimalView, AnimalViewParams

urlpatterns = [
    path("animals/", AnimalView.as_view()),
    path("animals/<animal_id>", AnimalViewParams.as_view()),
]
