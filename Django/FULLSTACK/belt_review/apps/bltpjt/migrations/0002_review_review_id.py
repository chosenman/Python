# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-28 07:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bltpjt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_id',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='reviewed', to='bltpjt.Book'),
            preserve_default=False,
        ),
    ]
