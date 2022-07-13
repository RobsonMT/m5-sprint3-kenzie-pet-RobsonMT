from django.forms import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status

from animals.models import Animal
from animals.serializers import AnimalSerializer


class AnimalView(APIView):
    def get(self, _: Request):
        animal = Animal.objects.all()
        serialized = AnimalSerializer(instance=animal, many=True)

        return Response(serialized.data, status.HTTP_200_OK)

    def post(self, request: Request):

        serialized = AnimalSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()

        return Response(serialized.data, status.HTTP_201_CREATED)


class AnimalViewParams(APIView):
    def get(self, _, animal_id):
        try:
            animal = get_object_or_404(Animal, pk=animal_id)
        except ValidationError as error:
            return Response({"error": error}, status=status.HTTP_404_NOT_FOUND)

        serialized = AnimalSerializer(animal)

        return Response(serialized.data, status.HTTP_200_OK)

    def patch(self, request, animal_id):
        try:
            animal = get_object_or_404(Animal, pk=animal_id)
        except ValidationError as error:
            return Response({"error": error}, status=status.HTTP_404_NOT_FOUND)

        serialized = AnimalSerializer(animal, request.data, partial=True)
        serialized.is_valid(raise_exception=True)
        serialized.save()

        return Response(serialized.data)

    def delete(self, _, animal_id):
        try:
            animal = get_object_or_404(Animal, pk=animal_id)
        except ValidationError as error:
            return Response({"error": error}, status=status.HTTP_404_NOT_FOUND)

        animal.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
