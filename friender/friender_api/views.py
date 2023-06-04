from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from arrangement.models import Establishments, Users, Hobbies
from .serializers import EstablishmentSerializer, UsersSerializer, HobbiesSerializer
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication, TokenAuthentication


class EstablishmentAPIView(APIView):
    authentication_classes = [TokenAuthentication]

    def get_object(self, pk):
        try:
            return Establishments.objects.get(pk=pk)
        except Establishments.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        place = Establishments.objects.all()
        serializer_data = EstablishmentSerializer(place, many=True).data
        return Response(serializer_data)

    def post(self, request, format=None):
        serializer = EstablishmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        place = self.get_object(pk)
        serializer = EstablishmentSerializer(place, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        place = self.get_object(pk)
        place.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request, format=None):
        place = Users.objects.all()
        serializer_data = UsersSerializer(place, many=True).data
        return Response(serializer_data)

    def post(self, request, format=None):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class EstablishmentListAPIView(generics.ListCreateAPIView):
#     queryset = Establishments.objects.all()
#     serializer_class = EstablishmentSerializer
#
#
class EstablishmentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Establishments.objects.all()
    serializer_class = EstablishmentSerializer


@api_view()
def HobbiesAPIView(request):
    hobbies = Hobbies.objects.all()
    serializer = HobbiesSerializer(hobbies, many=True).data
    return Response(serializer)
