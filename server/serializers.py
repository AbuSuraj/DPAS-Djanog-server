# serializers.py

from rest_framework import serializers
from .models import YourModelName

class YourModelNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourModelName
        fields = '__all__'
