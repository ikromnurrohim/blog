# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-23 15:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0003_auto_20200623_0743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artikel',
            old_name='body',
            new_name='isi',
        ),
        migrations.RenameField(
            model_name='artikel',
            old_name='author',
            new_name='penulis',
        ),
        migrations.RenameField(
            model_name='artikel',
            old_name='upload',
            new_name='published',
        ),
        migrations.RenameField(
            model_name='artikel',
            old_name='timestamp',
            new_name='updated',
        ),
    ]