# Generated by Django 3.0.5 on 2020-04-28 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20200424_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcomment',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='projectcomment',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]