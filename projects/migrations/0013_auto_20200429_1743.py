# Generated by Django 3.0.5 on 2020-04-29 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20200429_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='requirement_links',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
