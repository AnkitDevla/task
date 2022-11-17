# Generated by Django 4.1.3 on 2022-11-16 07:46

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskApi', '0006_rename_created_date_task_created_at_task_udated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='id',
            field=models.IntegerField(default=builtins.id, primary_key=True, serialize=False, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='taskId',
            field=models.IntegerField(unique=True),
        ),
    ]