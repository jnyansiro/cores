# Generated by Django 3.0.5 on 2020-04-28 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_member_job_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmembership',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='projectmembership',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
