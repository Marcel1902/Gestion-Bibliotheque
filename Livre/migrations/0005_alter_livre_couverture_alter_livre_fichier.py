# Generated by Django 4.2.7 on 2023-12-28 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Livre', '0004_alter_livre_date_de_production'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livre',
            name='Couverture',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='livre',
            name='Fichier',
            field=models.FileField(upload_to='media'),
        ),
    ]