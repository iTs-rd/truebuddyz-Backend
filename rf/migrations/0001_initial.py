# Generated by Django 3.1.2 on 2021-09-13 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RfQuestionBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('que', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RfRoomDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('roomId', models.CharField(max_length=20)),
                ('playerId', models.CharField(max_length=20)),
                ('playerName', models.CharField(max_length=20)),
            ],
            options={
                'unique_together': {('roomId', 'playerId')},
                'index_together': {('roomId', 'playerId')},
            },
        ),
    ]
