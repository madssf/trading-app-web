# Generated by Django 3.2.4 on 2021-08-11 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0003_auto_20210809_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='modifiied',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
