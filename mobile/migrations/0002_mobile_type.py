# Generated by Django 4.1.13 on 2024-03-17 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile',
            name='type',
            field=models.CharField(default='mobile', max_length=255),
        ),
    ]