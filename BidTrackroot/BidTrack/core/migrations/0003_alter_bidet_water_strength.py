# Generated by Django 5.0.7 on 2024-07-16 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_bidet_water_strength_alter_bidet_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidet',
            name='water_strength',
            field=models.IntegerField(choices=[(5, 'Tsunami Blast'), (4, 'Power Wash'), (3, 'Moderate Stream'), (2, 'Light Drizzle'), (1, 'Gentle Mist')]),
        ),
    ]
