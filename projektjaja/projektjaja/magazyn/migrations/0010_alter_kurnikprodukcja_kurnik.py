# Generated by Django 4.0.4 on 2022-07-03 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazyn', '0009_kurnikprodukcja_kurnik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kurnikprodukcja',
            name='Kurnik',
            field=models.CharField(choices=[('K1', 'Kurnik K1'), ('K3', 'Kurnik K3')], default='Kurnik K3', max_length=10),
        ),
    ]
