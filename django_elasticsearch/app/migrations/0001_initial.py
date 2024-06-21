# Generated by Django 5.0.6 on 2024-05-15 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('author', models.CharField(max_length=1000)),
                ('description', models.TextField()),
            ],
        ),
    ]
