# Generated by Django 4.1 on 2022-08-31 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meseros', '0002_meseros_edad'),
    ]

    operations = [
        migrations.AddField(
            model_name='meseros',
            name='procedencia',
            field=models.CharField(default='', max_length=40),
        ),
    ]