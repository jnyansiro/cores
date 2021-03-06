# Generated by Django 3.1b1 on 2020-07-08 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0026_stakeholder_project'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ScenarioStackholder',
            new_name='ProcessStakeholder',
        ),
        migrations.RenameModel(
            old_name='UsecaseStackholder',
            new_name='RequirementStakeholder',
        ),
        migrations.RenameModel(
            old_name='ProcessStackholder',
            new_name='ScenarioStakeholder',
        ),
        migrations.RenameModel(
            old_name='RequirementStackholder',
            new_name='UsecaseStakeholder',
        ),
        migrations.RemoveField(
            model_name='processstakeholder',
            name='scenario',
        ),
        migrations.RemoveField(
            model_name='requirementstakeholder',
            name='usecase',
        ),
        migrations.RemoveField(
            model_name='scenariostakeholder',
            name='process',
        ),
        migrations.RemoveField(
            model_name='usecasestakeholder',
            name='requirement',
        ),
        migrations.AddField(
            model_name='processstakeholder',
            name='process',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.process'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requirementstakeholder',
            name='requirement',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.requirement'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scenariostakeholder',
            name='scenario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.scenario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usecasestakeholder',
            name='usecase',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.usecase'),
            preserve_default=False,
        ),
    ]
