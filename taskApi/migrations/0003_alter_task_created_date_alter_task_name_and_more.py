# Generated by Django 4.1.3 on 2022-11-16 04:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskApi', '0002_alter_task_created_date_alter_task_taskid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 16, 10, 10, 46, 157467)),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='taskId',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
