# Generated by Django 3.0.5 on 2020-05-04 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_auto_20200501_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='starrate',
            name='rate_status',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
