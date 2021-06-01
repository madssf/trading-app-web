# Generated by Django 3.2.3 on 2021-05-30 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0004_auto_20210530_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolioasset',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='portfolioasset',
            name='status',
        ),
        migrations.AddField(
            model_name='portfolioasset',
            name='flex',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=18, null=True),
        ),
        migrations.AddField(
            model_name='portfolioasset',
            name='locked',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=18, null=True),
        ),
        migrations.AddField(
            model_name='portfolioasset',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='portfolioasset',
            name='spot',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=18, null=True),
        ),
        migrations.AlterField(
            model_name='portfolioasset',
            name='average',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=18, null=True),
        ),
    ]