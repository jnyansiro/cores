# Generated by Django 3.1b1 on 2020-06-28 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20200628_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginlog',
            name='logout_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
