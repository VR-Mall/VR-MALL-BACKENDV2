from django.shortcuts import render
from rest_framework import generics
from .models import Business
from .serializers import BusinessSerializer

class BusinessList(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class BusinessDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Business.objects.all()    
    serializer_class = BusinessSerializer
