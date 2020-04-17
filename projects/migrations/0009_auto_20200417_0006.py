# Generated by Django 3.0.2 on 2020-04-17 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20200416_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewpoint',
            name='viewpoint_docs',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viewpoint',
            name='viewpoint_links',
            field=models.CharField(default=1, max_length=600),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viewpoint',
            name='viewpoint_photo',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]