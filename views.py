from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import KitabPost, BabPost, FasalPost
from .serializers import KitabPostSerializer, BabPostSerializer, FasalPostSerializer
from rest_framework.views import APIView

class KitabPostListCreate(generics.ListCreateAPIView):
    queryset = KitabPost.objects.all()
    serializer_class = KitabPostSerializer

    def delete(self, request, *args, **kwargs):
        KitabPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class KitabPostRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = KitabPost.objects.all()
    serializer_class = KitabPostSerializer
    lookup_field = "pk"

class KitabPostlist(APIView):
    def get(self, request, format=None):
        KitabPost = KitabPost.object.all()
        serializer = KitabPostSerializer(KitabPost, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = KitabPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BabPostListCreate(generics.ListCreateAPIView):
    queryset = BabPost.objects.all()
    serializer_class = BabPostSerializer

    def delete(self, request):
        BabPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BabPostRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = BabPost.objects.all()
    serializer_class = BabPostSerializer
    lookup_field = "pk"   

class BabPostlist(APIView):
    def get(self, request, format=None):
        BabPost = BabPost.object.all()
        serializer = BabPostSerializer(BabPost, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BabPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FasalPostListCreate(generics.ListCreateAPIView):
    queryset = FasalPost.objects.all()
    serializer_class = FasalPostSerializer

    def delete(self, request):
        FasalPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FasalPostRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = FasalPost.objects.all()
    serializer_class = FasalPostSerializer
    lookup_field = "pk" 

class FasalPostlist(APIView):
    def get(self, request, format=None):
        FasalPost = FasalPost.object.all()
        serializer = FasalPostSerializer(FasalPost, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FasalPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

# Create your views here.
