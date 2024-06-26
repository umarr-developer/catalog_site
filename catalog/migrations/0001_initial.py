# Generated by Django 5.0.4 on 2024-05-27 09:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('image', models.FileField(upload_to='files/')),
                ('characteristic', models.JSONField()),
                ('price', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('create_on', models.DateField(auto_now_add=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.brand')),
            ],
        ),
    ]
