# Generated by Django 3.2 on 2022-02-22 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.IntegerField(max_length=11, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('point', models.CharField(max_length=11)),
                ('help', models.CharField(max_length=11)),
                ('bank', models.CharField(max_length=11)),
            ],
        ),
    ]
