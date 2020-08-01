# Generated by Django 3.1rc1 on 2020-07-22 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0035_auto_20200720_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScenarioUsecase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.scenario')),
                ('usecase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.usecase')),
            ],
        ),
        migrations.CreateModel(
            name='ScenarioProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.process')),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.scenario')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessUsecase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.process')),
                ('usecase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.usecase')),
            ],
        ),
    ]