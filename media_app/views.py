from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import MediaItem
from .serializers import MediaItemSerializer

class MediaItemViewSet(viewsets.ModelViewSet):
    queryset = MediaItem.objects.all()
    serializer_class = MediaItemSerializer
    parser_classes = (MultiPartParser, FormParser)  # поддержка upload
