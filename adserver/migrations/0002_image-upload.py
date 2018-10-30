# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-29 23:49
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('adserver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(blank=True, help_text='240x180', max_length=255, null=True, upload_to='%Y/%m/', verbose_name='Image'),
        ),
    ]
