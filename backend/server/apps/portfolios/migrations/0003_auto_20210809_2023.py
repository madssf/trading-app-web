# Generated by Django 3.2.4 on 2021-08-09 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0002_auto_20210802_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='balanced_portfolio',
            field=models.JSONField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='instructions',
            field=models.JSONField(blank=True, default=None, null=True),
        ),
    ]
