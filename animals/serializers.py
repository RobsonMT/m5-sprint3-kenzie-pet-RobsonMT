from rest_framework import serializers

from animals.models import Animal
from groups.models import Group
from characteristics.models import Characteristic
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
        attrs["name"] = attrs["name"].capitalize()
        attrs["sex"] = attrs["name"].lower()
        return super().validate(attrs)

    def create(self, validated_data):

        group_data = validated_data.pop("group")
        characteristics_data = validated_data.pop("characteristics")

        group, _ = Group.objects.get_or_create(**group_data)

        animal = Animal.objects.create(group_id=group.id, **validated_data)

        for char in characteristics_data:
            char, _ = Characteristic.objects.get_or_create(**char)
            animal.characteristics.add(char)

        return animal

    def update(self, instance, validated_data):

        if "group" in validated_data:
            group_data = validated_data.pop("group")
            group, _ = Group.objects.get_or_create(**group_data)
            instance.group = group

        if "characteristics" in validated_data:
            instance.characteristics.clear()

            characteristics_data = validated_data.pop("characteristics")
            for char in characteristics_data:
                char, _ = Characteristic.objects.get_or_create(**char)
                instance.characteristics.add(char)

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance
