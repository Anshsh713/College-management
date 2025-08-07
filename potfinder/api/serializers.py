from rest_framework import serializers
from .models import Task  # ensure Task is defined in your models.py

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
