# Generated by Django 3.0.2 on 2020-04-14 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200414_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(max_length=50),
        ),
    ]
