# Generated by Django 3.2.4 on 2021-06-06 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0004_auto_20210605_1654'),
        ('exchanges', '0001_initial'),
        ('portfolios', '0007_alter_portfolioasset_status'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='portfolioasset',
            unique_together={('portfolio', 'currency', 'exchange', 'close_time', 'stake_end', 'stake_start', 'apr')},
        ),
    ]