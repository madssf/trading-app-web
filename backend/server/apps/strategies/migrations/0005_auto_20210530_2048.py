# Generated by Django 3.2.3 on 2021-05-30 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategies', '0004_alter_strategy_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameter',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='parametertype',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='strategyparameter',
            unique_together={('parameter', 'strategy')},
        ),
    ]
