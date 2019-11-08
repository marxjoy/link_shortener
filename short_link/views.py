from rest_framework import generics
from .models import Link
from .serializers import LinkSerializer

class LinkListView(generics.ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class LinkDetailView(generics.RetrieveAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

