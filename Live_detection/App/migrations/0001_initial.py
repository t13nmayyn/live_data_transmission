# Generated by Django 5.0.7 on 2025-02-13 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Display',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('array', models.JSONField()),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
