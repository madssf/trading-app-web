# Generated by Django 3.2.3 on 2021-05-25 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('strategies', '0002_parametertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
                ('parameter_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategies.parametertype')),
            ],
        ),
        migrations.CreateModel(
            name='StrategyParameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategies.parameter')),
                ('strategy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategies.strategy')),
            ],
        ),
    ]