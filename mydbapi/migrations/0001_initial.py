# Generated by Django 3.0.9 on 2020-08-04 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('userid', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('passwordhash', models.CharField(max_length=256)),
            ],
        ),
    ]