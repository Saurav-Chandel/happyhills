# Generated by Django 3.2.19 on 2023-08-15 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0014_auto_20230808_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='iternary',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='treks',
            name='best_season',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
