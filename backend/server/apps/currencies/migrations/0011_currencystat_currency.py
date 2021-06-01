# Generated by Django 3.2.3 on 2021-05-31 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0010_currencystat_mcaptotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='currencystat',
            name='currency',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='currencies.currency'),
            preserve_default=False,
        ),
    ]