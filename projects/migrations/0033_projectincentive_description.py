# Generated by Django 3.0.8 on 2020-07-18 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0032_auto_20200712_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectincentive',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
