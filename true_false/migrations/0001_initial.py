# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-07 18:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quiz', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='TF_Question',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='quiz.Question')),
                ('correct', models.BooleanField(default=False, help_text='Tick this if the question is true. Leave it blank for false.', verbose_name='Correct')),
            ],
            options={
                'ordering': ['category'],
                'verbose_name': 'True/False Question',
                'verbose_name_plural': 'True/False Questions',
            },
            bases=('quiz.question',),
        ),
    ]
