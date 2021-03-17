from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Home
from .serializations import HomeSerializers
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class HomeViews(APIView):
    def get(self, request, pk=None):
        id = pk
        if id is not None:
            hom = Home.objects.get(id=id)
            serializer = HomeSerializers(hom)
            return Response(serializer.data)
        hom = Home.objects.all()
        serializer = HomeSerializers(hom, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HomeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk = None):
        id = pk
        hom = Home.objects.get(id=id)
        serializer = HomeSerializers(hom, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request):
        hom = Home.objects.get(pk=id)
        serializer = HomeSerializers(hom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request , pk=None):
        id = pk
        hom = Home.objects.get(id=id)
        hom.delete()
        return Response({'msg': 'Deleted Success'})
