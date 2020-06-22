from django.shortcuts import render

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Rekomendacje
from .serializers import RecomendationsSerializers


from .models import Zamowienia
from .serializers import OrderSerializers

from .models import Wiadomosci
from .serializers import MessageSerializers

from .serializers import NewsletterSerializers


from .models import Blog
from .serializers import BlogSerializers

class Recomendations(APIView):
    def get(self, request, format=None):
        recomendations = Rekomendacje.objects.all()
        serializer = RecomendationsSerializers(recomendations, many=True)
        return Response(serializer.data)

class BlogPosts(APIView):
    def get(self, request, format=None):
        blogPosts = Blog.objects.all()
        serializer = BlogSerializers(blogPosts, many=True)
        return Response(serializer.data)

class Order(APIView):
    def get(self, request, format=None):
        orders= Zamowienia.objects.all()
        serializer = OrderSerializers(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Message(APIView):
    def post(self, request, format=None):
        serializer = MessageSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Newsletter(APIView):
    def post(self, request, format=None):
        serializer = NewsletterSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


