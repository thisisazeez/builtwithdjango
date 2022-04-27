# Generated by Django 3.0.6 on 2021-05-28 15:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="author",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="comment",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="projects.Project",
            ),
        ),
    ]
