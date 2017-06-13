# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-12 20:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20170612_2153'),
        ('blog', '0004_blogpage_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPeopleRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_person_relationship', to='blog.BlogPage')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_blog_relationship', to='home.People')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
