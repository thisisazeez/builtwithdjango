# Generated by Django 3.2.4 on 2021-08-13 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("podcast", "0005_auto_20210813_0303"),
    ]

    operations = [
        migrations.AlterField(
            model_name="episode",
            name="details",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="episode",
            name="player_html_embed",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="episode",
            name="show_notes",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="episode",
            name="transcript",
            field=models.TextField(blank=True),
        ),
    ]
