# Generated by Django 3.0.6 on 2020-05-16 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0029_auto_20200516_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='institution_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]