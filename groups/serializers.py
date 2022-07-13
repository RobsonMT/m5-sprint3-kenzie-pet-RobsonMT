from rest_framework import serializers


class GroupSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=20)
    scientific_name = serializers.CharField(max_length=50)

    def validate(self, attrs):
        attrs["name"] = attrs["name"].capitalize()
        attrs["scientific_name"] = attrs["scientific_name"].capitalize()
        return super().validate(attrs)
