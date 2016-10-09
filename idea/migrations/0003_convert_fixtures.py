# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def insert_config(apps, schema_editor):
    Config = apps.get_model("idea", "Config")
    list_about = Config()
    list_about.pk = 1
    list_about.key = 'list_about'
    list_about.value = 'IdeaBox is a place where everyone in the CFPB can share their ideas on how to improve the work we do for consumers and the way we do it. Challenges give you the opportunity to share your solution to a specific problem. Submit your ideas and join the conversation!'
    list_about.save()


def insert_state(apps, schema_editor):
    State = apps.get_model("idea", "State")
    active = State()
    active.pk = 1
    active.name = 'Active'
    active.save()

    archive = State()
    archive.pk = 2
    archive.name = 'Archive'
    archive.previous = active
    archive.save()


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0002_auto_20160926_1824'),
    ]

    operations = [
        migrations.RunPython(insert_config),
        migrations.RunPython(insert_state)
    ]