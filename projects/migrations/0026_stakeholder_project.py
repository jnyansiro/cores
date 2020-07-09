# Generated by Django 3.1b1 on 2020-07-08 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0025_processstackholder_requirementstackholder_scenariostackholder_stakeholder_usecasestackholder'),
    ]

    operations = [
        migrations.AddField(
            model_name='stakeholder',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
            preserve_default=False,
        ),
    ]
