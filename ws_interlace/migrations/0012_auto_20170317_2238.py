# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 22:38
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ws_interlace', '0011_remove_answer_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worksheet',
            name='title',
        ),
        migrations.AlterField(
            model_name='worksheet',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]