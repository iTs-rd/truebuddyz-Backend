# Generated by Django 3.2.2 on 2021-09-20 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('howwelluknow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='howwelluknow',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='howwelluknowscore',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]