# Generated by Django 3.0 on 2019-12-04 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20191204_0555'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='author_github',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='draft',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='project',
            name='website_additional_info',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='author_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='project',
            name='author_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='website_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='website_homepage_screenshot',
            field=models.ImageField(blank=True, upload_to='website_homepage_screenshot/'),
        ),
    ]
