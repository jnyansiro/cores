# Generated by Django 3.1b1 on 2020-07-04 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_auto_20200704_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='viewpoint',
        ),
        migrations.RemoveField(
            model_name='requirement',
            name='goal',
        ),
    ]
