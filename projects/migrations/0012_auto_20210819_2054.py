# Generated by Django 3.2.4 on 2021-08-19 20:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("podcast", "0010_alter_episode_maker"),
        ("makers", "0002_alter_maker_table"),
        ("projects", "0011_alter_project_technologies"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="maker",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="makers.maker",
            ),
        ),
        migrations.DeleteModel(
            name="Maker",
        ),
    ]
