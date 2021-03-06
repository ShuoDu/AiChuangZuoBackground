# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-22 15:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sucai', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='author',
            field=models.CharField(max_length=100, null=True, verbose_name='\u4f5c\u8005'),
        ),
        migrations.AlterField(
            model_name='message',
            name='author_img',
            field=models.CharField(max_length=300, null=True, verbose_name='\u4f5c\u8005\u5934\u50cf\u94fe\u63a5'),
        ),
        migrations.AlterField(
            model_name='message',
            name='deck_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sucai.deck_type', verbose_name='\u5e73\u53f0'),
        ),
        migrations.AlterField(
            model_name='message',
            name='field_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sucai.field_type', verbose_name='\u9886\u57df'),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_content',
            field=models.CharField(max_length=8000, null=True, verbose_name='\u6d88\u606f\u5185\u5bb9'),
        ),
    ]
