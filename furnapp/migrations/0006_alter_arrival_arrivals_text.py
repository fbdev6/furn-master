# Generated by Django 4.0.6 on 2022-08-15 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnapp', '0005_alter_arrival_arrivals_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arrival',
            name='arrivals_text',
            field=models.TextField(max_length=700),
        ),
    ]
