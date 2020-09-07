from rest_framework import serializers
from plants.models import Picture


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ("image",)

    def create(self, validated_data):
        pass
