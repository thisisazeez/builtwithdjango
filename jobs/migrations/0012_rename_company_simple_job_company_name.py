# Generated by Django 3.2.9 on 2021-11-22 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0011_job_company_simple"),
    ]

    operations = [
        migrations.RenameField(
            model_name="job",
            old_name="company_simple",
            new_name="company_name",
        ),
    ]