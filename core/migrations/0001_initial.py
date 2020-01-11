# Generated by Django 3.0.2 on 2020-01-11 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('published_at', models.DateTimeField()),
            ],
        ),
    ]
