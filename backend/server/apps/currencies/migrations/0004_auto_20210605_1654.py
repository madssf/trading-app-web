# Generated by Django 3.2.4 on 2021-06-05 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0003_alter_currency_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currency',
            old_name='mcap_total',
            new_name='mcap',
        ),
        migrations.RemoveField(
            model_name='currency',
            name='slug',
        ),
    ]
