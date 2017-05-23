# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0001_initial'),
        ('reactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagereaction',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='imagereaction',
            name='episode',
            field=models.ForeignKey(null=True, to='episodes.Episode'),
        ),
        migrations.AddField(
            model_name='tweetreaction',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tweetreaction',
            name='episode',
            field=models.ForeignKey(null=True, to='episodes.Episode'),
        ),
    ]
