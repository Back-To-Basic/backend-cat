from rest_framework import serializers

from .models import AnimalImage


class AnimalImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnimalImage
        fields = '__all__'
