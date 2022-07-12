from rest_framework import serializers


class GroupSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=20)
    scientific_name = serializers.CharField(max_length=50)

    def validate(self, attrs):
        print(attrs, "attrs")
        return super().validate(attrs)
