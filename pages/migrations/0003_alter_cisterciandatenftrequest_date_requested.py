# Generated by Django 3.2.4 on 2021-09-14 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0002_alter_cisterciandatenftrequest_wallet_public_key"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cisterciandatenftrequest",
            name="date_requested",
            field=models.DateField(unique=True),
        ),
    ]
