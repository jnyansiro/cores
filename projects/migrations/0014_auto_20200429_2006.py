# Generated by Django 3.0.5 on 2020-04-29 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20200429_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]