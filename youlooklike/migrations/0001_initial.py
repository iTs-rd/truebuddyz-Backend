# Generated by Django 3.1.2 on 2021-09-28 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YouLookLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('que1', models.CharField(max_length=200)),
                ('option1A', models.CharField(max_length=80)),
                ('option1B', models.CharField(max_length=80)),
                ('option1C', models.CharField(blank=True, max_length=80, null=True)),
                ('option1D', models.CharField(blank=True, max_length=80, null=True)),
                ('image1', models.CharField(blank=True, max_length=600, null=True)),
                ('que2', models.CharField(max_length=200)),
                ('option2A', models.CharField(max_length=80)),
                ('option2B', models.CharField(max_length=80)),
                ('option2C', models.CharField(blank=True, max_length=80, null=True)),
                ('option2D', models.CharField(blank=True, max_length=80, null=True)),
                ('image2', models.CharField(blank=True, max_length=600, null=True)),
                ('que3', models.CharField(max_length=200)),
                ('option3A', models.CharField(max_length=80)),
                ('option3B', models.CharField(max_length=80)),
                ('option3C', models.CharField(blank=True, max_length=80, null=True)),
                ('option3D', models.CharField(blank=True, max_length=80, null=True)),
                ('image3', models.CharField(blank=True, max_length=600, null=True)),
                ('que4', models.CharField(max_length=200)),
                ('option4A', models.CharField(max_length=80)),
                ('option4B', models.CharField(max_length=80)),
                ('option4C', models.CharField(blank=True, max_length=80, null=True)),
                ('option4D', models.CharField(blank=True, max_length=80, null=True)),
                ('image4', models.CharField(blank=True, max_length=600, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='YouLookLikeRandom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('que', models.CharField(max_length=200)),
                ('optionA', models.CharField(max_length=80)),
                ('optionB', models.CharField(max_length=80)),
                ('optionC', models.CharField(blank=True, max_length=80, null=True)),
                ('optionD', models.CharField(blank=True, max_length=80, null=True)),
                ('image', models.CharField(blank=True, max_length=600, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='YouLookLikeScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=40)),
                ('image', models.CharField(max_length=600)),
                ('text', models.CharField(max_length=200)),
            ],
        ),
    ]
