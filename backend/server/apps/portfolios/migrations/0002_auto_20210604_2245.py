# Generated by Django 3.2.4 on 2021-06-04 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolioasset',
            name='active',
        ),
        migrations.RemoveField(
            model_name='portfolioasset',
            name='flex',
        ),
        migrations.RemoveField(
            model_name='portfolioasset',
            name='flex_apr',
        ),
        migrations.RemoveField(
            model_name='portfolioasset',
            name='flex_start',
        ),
        migrations.RemoveField(
            model_name='portfolioasset',
            name='locked',
        ),
        migrations.RemoveField(
            model_name='portfolioasset',
            name='locked_apr',
        ),
        migrations.RemoveField(
            model_name='portfolioasset',
            name='locked_end',
        ),
        migrations.RemoveField(
            model_name='portfolioasset',
            name='locked_start',
        ),
        migrations.RemoveField(
            model_name='portfolioasset',
            name='spot',
        ),
        migrations.RemoveField(
            model_name='portfolioasset',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='portfolioasset',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=18, null=True),
        ),
        migrations.AddField(
            model_name='portfolioasset',
            name='apr',
            field=models.DecimalField(blank=True, decimal_places=4, default=0, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='portfolioasset',
            name='close_time',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portfolioasset',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='portfolioasset',
            name='stake_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portfolioasset',
            name='stake_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portfolioasset',
            name='status',
            field=models.CharField(choices=[('SPOT', 'Tradeable instantly.'), ('FLEX', 'Trade able with action.'), ('LOCK', 'Not tradeable.')], default='SPOT', max_length=4),
        ),
        migrations.CreateModel(
            name='PortfolioLogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('assets', models.JSONField()),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolios.portfolio')),
            ],
            options={
                'verbose_name_plural': 'Portfolio Log Entries',
            },
        ),
    ]