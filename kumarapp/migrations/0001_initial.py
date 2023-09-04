# Generated by Django 3.0 on 2023-09-02 17:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('age', models.IntegerField(max_length=3)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('created_at', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]