# Generated by Django 3.1b1 on 2020-07-12 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0028_auto_20200712_1642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='viewpointdislike',
            old_name='viewpoint',
            new_name='view_point',
        ),
    ]