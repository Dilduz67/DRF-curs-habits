# Generated by Django 4.2.3 on 2024-03-30 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.TimeField(verbose_name='время для привычки'),
        ),
    ]