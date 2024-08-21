# Generated by Django 4.2.15 on 2024-08-21 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Well',
            fields=[
                ('well', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('oil', models.IntegerField()),
                ('gas', models.IntegerField()),
                ('brine', models.IntegerField()),
            ],
        ),
    ]
