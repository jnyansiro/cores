# Generated by Django 3.0.5 on 2020-04-29 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20200428_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='goal_link',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]