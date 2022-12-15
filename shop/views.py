from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

# Create your views here.
from .models import Category,Firm,Item
from .serializers import CategorySerializer,FirmSerializer,ItemSerializer

class CategoryApiView(APIView):
    def get(self,request,*args,**kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):
    def get_object(self):
        return get_object_or_404(Category,id=self.kwargs.get('id'))
    def get(self,request,*args,**kwargs):
        serializer = CategorySerializer(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,*args,**kwargs):
        serializer = CategorySerializer(self.get_object(),data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FirmApiView(APIView):
    def get(self, request, *args, **kwargs):
        firms = Firm.objects.all()
        serializer = FirmSerializer(firms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = FirmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FirmDetailView(APIView):
    def get_object(self):
        return get_object_or_404(Firm, id=self.kwargs.get('id'))

    def get(self, request, *args, **kwargs):
        serializer = FirmSerializer(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        serializer = FirmSerializer(self.get_object(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ItemApiView(APIView):
    def get(self, request, *args, **kwargs):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = FirmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemDetailView(APIView):
    def get_object(self):
        return get_object_or_404(Item, id=self.kwargs.get('id'))

    def get(self, request, *args, **kwargs):
        serializer = ItemSerializer(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        serializer = ItemSerializer(self.get_object(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



