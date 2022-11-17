from rest_framework import serializers
from .models import task

class taskSerializer(serializers.ModelSerializer):
    class Meta:
        model=task
        fields=('taskId','name','priority','description','created_at','udated_at')


