# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categor\xeda', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=250, unique=True, null=True, verbose_name='Categor\xeda', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(verbose_name='Categor\xeda', blank=True, to='quiz.Category', null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='category',
            field=models.ForeignKey(verbose_name='Categor\xeda', blank=True, to='quiz.Category', null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.CharField(max_length=60, verbose_name='T\xedtulo'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(verbose_name='Categor\xeda', blank=True, to='quiz.Category', null=True),
        ),
    ]
