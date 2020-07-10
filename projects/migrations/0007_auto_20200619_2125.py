# Generated by Django 3.1b1 on 2020-06-19 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20200619_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='process',
            name='requirement',
        ),
        migrations.RemoveField(
            model_name='scenario',
            name='requirement',
        ),
        migrations.RemoveField(
            model_name='usecase',
            name='requirement',
        ),
        migrations.CreateModel(
            name='RequirementUsecase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('requirement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.requirement')),
                ('usecase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.usecase')),
            ],
        ),
        migrations.CreateModel(
            name='RequirementScenario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.requirement')),
            ],
        ),
        migrations.CreateModel(
            name='RequirementProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.process')),
                ('requirement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.requirement')),
            ],
        ),
    ]