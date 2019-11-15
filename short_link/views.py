from rest_framework import generics
from rest_framework.views import APIView
from .models import Link
from .serializers import LinkSerializer
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from rest_framework.response import Response


class LinkListView(generics.ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class LinkDetailView(DetailView):
    model = Link



class LinkAPIView(APIView):
    def post(self, request):
        url = request.query_params['url']
        link = Link.objects.create(original_url=url)
        link.save()
        return Response({'r': url})


    def head(self, request):
        return None

    def get(self, request):
        link = Link.objects.filter()
        return link

    def delete(self, request):
        return None



class LinkHomeView(CreateView):
    model = Link
    fields = ['original_url']