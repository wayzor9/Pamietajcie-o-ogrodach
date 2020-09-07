from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import PictureSerializer
from .models import Picture


class PictureViewSet(viewsets.ViewSet):
    serializer_class = PictureSerializer
    queryset = Picture.objects.all()
