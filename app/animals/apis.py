from rest_framework import mixins, viewsets

from .models import AnimalImage
from .serializers import AnimalImagesSerializer


class AnimalImageViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = AnimalImage.objects.all()
    serializer_class_mapping = {
        'list': AnimalImagesSerializer,
        'retrieve': AnimalImagesSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_class_mapping.get(self.action)
