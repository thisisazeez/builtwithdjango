# Generated by Django 3.2.4 on 2021-09-15 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0003_alter_cisterciandatenftrequest_date_requested"),
    ]

    operations = [
        migrations.AddField(
            model_name="cisterciandatenftrequest",
            name="link",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="cisterciandatenftrequest",
            name="proof",
            field=models.URLField(blank=True),
        ),
    ]
