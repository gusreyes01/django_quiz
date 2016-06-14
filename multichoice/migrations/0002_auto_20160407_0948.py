# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multichoice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='content',
            field=models.CharField(help_text='Enter the answer text that you want displayed', max_length=1000, verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='mcquestion',
            name='answer_order',
            field=models.CharField(choices=[('content', 'Contenido'), ('random', 'Random'), ('none', 'Ninguno')], max_length=30, blank=True, help_text='The order in which multichoice answer options are displayed to the user', null=True, verbose_name='Answer Order'),
        ),
    ]
