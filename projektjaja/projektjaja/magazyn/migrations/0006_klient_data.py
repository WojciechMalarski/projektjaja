# Generated by Django 4.0.4 on 2022-07-01 08:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazyn', '0005_suma_klient'),
    ]

    operations = [
        migrations.AddField(
            model_name='klient',
            name='Data',
            field=models.DateField(default=datetime.date(2022, 7, 1)),
        ),
    ]
