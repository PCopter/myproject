# Generated by Django 5.0.4 on 2024-07-08 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_standard', '0002_country_itemtest_specification_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specification',
            name='name',
        ),
        migrations.AddField(
            model_name='specification',
            name='description',
            field=models.TextField(default="Don't forget to fill out the information.", max_length=500),
        ),
    ]