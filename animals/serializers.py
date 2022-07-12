from uuid import uuid4
from rest_framework import serializers

from animals.models import Animal
from groups.models import Group
from characteristics.serializers import CharacteristicSerializer
from groups.serializers import GroupSerializer


class AnimalSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField(max_length=15)
    group = GroupSerializer()
    characteristics = CharacteristicSerializer(many=True)

    def validate(self, attrs):
        print(attrs, "attrs")
        return super().validate(attrs)
