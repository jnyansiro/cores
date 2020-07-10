# Generated by Django 3.1b1 on 2020-07-08 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0024_auto_20200706_0019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stakeholder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.member')),
            ],
        ),
        migrations.CreateModel(
            name='UsecaseStackholder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('stakeholder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.stakeholder')),
                ('usecase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.usecase')),
            ],
        ),
        migrations.CreateModel(
            name='ScenarioStackholder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.scenario')),
                ('stakeholder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.stakeholder')),
            ],
        ),
        migrations.CreateModel(
            name='RequirementStackholder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('requirement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.requirement')),
                ('stakeholder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.stakeholder')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessStackholder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.process')),
                ('stakeholder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.stakeholder')),
            ],
        ),
    ]