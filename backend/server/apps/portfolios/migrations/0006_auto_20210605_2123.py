# Generated by Django 3.2.4 on 2021-06-05 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0005_remove_portfolioasset_average'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credentials',
            old_name='api_payload',
            new_name='data',
        ),
        migrations.RenameField(
            model_name='credentials',
            old_name='api_key',
            new_name='key',
        ),
        migrations.RenameField(
            model_name='credentials',
            old_name='api_secret',
            new_name='secret',
        ),
    ]