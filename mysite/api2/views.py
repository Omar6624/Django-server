from django.shortcuts import render
from rest_framework.views import APIView
from .models import DataShow
from .serializers import DataShowSerializer
from django.http import JsonResponse
from rest_framework.response import Response

class DataShowListCreate(APIView):
    def get(self,request):
        reports = DataShow.objects.all()
        serializer_class = DataShowSerializer(reports,many=True)
        return Response(serializer_class.data)