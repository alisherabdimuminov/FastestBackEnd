# Generated by Django 5.1.2 on 2024-10-29 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='score',
            field=models.IntegerField(default=1),
        ),
    ]
