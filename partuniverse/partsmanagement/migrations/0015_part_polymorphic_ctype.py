# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('partsmanagement', '0014_auto_20160426_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_partsmanagement.part_set+', to='contenttypes.ContentType'),
        ),
    ]