# Generated by Django 4.0.4 on 2022-07-01 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazyn', '0002_suma_cena1b_suma_cena2a_suma_cenas_suma_cenass_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suma',
            name='CenaS',
            field=models.IntegerField(default=190),
        ),
    ]