from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .serializers import TestSerializer
from .models import TestModel

from django.http import HttpResponse
# Create your views here.

#def main(request):
#    return HttpResponse("hello world")

class TestView(generics.ListAPIView): #CreateAPIView
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer
