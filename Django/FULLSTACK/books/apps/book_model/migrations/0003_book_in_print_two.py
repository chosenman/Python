# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 18:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book_model', '0002_book_in_print'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='in_print_two',
            field=models.BooleanField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
