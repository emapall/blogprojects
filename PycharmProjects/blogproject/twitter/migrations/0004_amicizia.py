# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('twitter', '0003_remove_tweet_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amicizia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_amicizia', models.DateTimeField(auto_now=True)),
                ('followed', models.ForeignKey(related_name='follower_set', to=settings.AUTH_USER_MODEL)),
                ('follower', models.ForeignKey(related_name='followed_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
