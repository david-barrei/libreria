# Generated by Django 3.2.25 on 2024-12-01 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resenia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resenia',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]