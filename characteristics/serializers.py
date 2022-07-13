from rest_framework import serializers


class CharacteristicSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=20)

    def validate(self, attrs):
        attrs["name"] = attrs["name"].lower()
        return super().validate(attrs)
