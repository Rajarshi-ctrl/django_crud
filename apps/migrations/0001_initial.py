# Generated by Django 3.2.3 on 2021-06-07 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=5000)),
                ('date', models.DateField()),
            ],
        ),
    ]
