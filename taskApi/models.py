from django.db import models
from datetime import datetime
from random import randint

priority_choice = (
    ('High', 'HIGH'),
    ('Medium', 'MEDIUM'),
    ('Low', 'LOW'),
)


class task(models.Model):
    taskId = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250,unique=True)
    priority = models.CharField(max_length=8, choices=priority_choice)
    description = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    udated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        