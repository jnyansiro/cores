# Generated by Django 3.1b1 on 2020-06-24 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_resetpassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
