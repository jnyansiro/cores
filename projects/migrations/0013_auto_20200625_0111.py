# Generated by Django 3.1b1 on 2020-06-24 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_comment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(default='pending', max_length=40),
        ),
    ]
