from rest_framework.views import APIView, Request, Response, status

from animals.models import Animal
from animals.serializers import AnimalSerializer


class AnimalView(APIView):
    def get(self, _: Request):
        animal = Animal.objects.all()

        serialized = AnimalSerializer(instance=animal, many=True)

        print(animal)

        return Response({"animals": serialized.data}, status.HTTP_200_OK)

    def post(self, request: Request):

        # print(request.data)

        # serialized = AnimalSerializer(data=request.data)
        # serialized.is_valid(raise_exception=True)

        # animal = Animal.objects.create(**serialized.validated_data)

        # serialized = AnimalSerializer(instance=animal)

        serialized = AnimalSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()  # metodo create do serializer

        return Response("serialized.data", status.HTTP_201_CREATED)
