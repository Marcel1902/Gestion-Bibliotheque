# Generated by Django 4.2.7 on 2023-12-22 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Livre', '0002_livre_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livre',
            name='Date_de_production',
            field=models.DateTimeField(blank=True),
        ),
    ]