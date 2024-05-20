from rest_framework import serializers
from .models import DataShow

class DataShowSerializer(serializers.ModelSerializer):
    class Meta:
        model=DataShow
        fields = '__all__'
