# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import idea.models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(editable=False, blank=True, unique=True, verbose_name='Slug')),
                ('text', models.TextField(max_length=2000, verbose_name=b'description')),
                ('start_date', models.DateField(help_text=b'The date from which this banner will be displayed.')),
                ('end_date', models.DateField(help_text=b'Empty indicates that the banner should be continued indefinitely. ', null=True, blank=True)),
                ('is_private', models.BooleanField(default=False, verbose_name=b'private room')),
                ('is_votes', models.BooleanField(default=True, verbose_name=b'voting enabled')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=50)),
                ('value', models.TextField(max_length=2000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(default=idea.models.set_to_now)),
                ('title', models.CharField(help_text=b'\n        Make your idea stand out from the rest with a good title.', max_length=50)),
                ('summary', models.TextField(help_text=b"\n        Get people's attention and instant support! Only the first 200\n        characters make it onto the IdeaBox landing page.", max_length=200)),
                ('text', models.TextField(help_text=b'\n        Describe your reasoning to garner deeper support. Include links to\n        any research, pages, or even other ideas.', max_length=2000, verbose_name=b'detail')),
                ('is_anonymous', models.BooleanField(default=False, help_text=b"\n        Only enable anonymous if the Idea's challenge is private", verbose_name=b'anonymous Idea')),
                ('banner', models.ForeignKey(verbose_name=b'challenge', blank=True, to='idea.Banner', null=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('previous', models.OneToOneField(null=True, blank=True, to='idea.State')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(default=idea.models.set_to_now)),
                ('vote', models.SmallIntegerField(default=1, choices=[('+1', 1)])),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('idea', models.ForeignKey(to='idea.Idea')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='idea',
            name='state',
            field=models.ForeignKey(to='idea.State'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='idea',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text=b'\n        Make it easy for supporters to find your idea.  See how many other\n        ideas have the same tags for potential collaboration or a little\n        healthy competition.', verbose_name='Tags'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='idea',
            name='voters',
            field=models.ManyToManyField(related_name=b'idea_vote_creator', null=True, through='idea.Vote', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
