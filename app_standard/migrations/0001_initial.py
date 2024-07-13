# Generated by Django 5.0.4 on 2024-05-08 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MinimumStandard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_test', models.CharField(max_length=100)),
                ('specification', models.TextField()),
                ('type', models.CharField(max_length=1)),
                ('thailand', models.BooleanField()),
                ('usa_canada', models.BooleanField()),
                ('malaysia', models.BooleanField()),
                ('indonisia', models.BooleanField()),
                ('europe_PED', models.BooleanField()),
                ('uae', models.BooleanField()),
                ('japan', models.BooleanField()),
                ('russia', models.BooleanField()),
                ('france_NF414', models.BooleanField()),
                ('philippines', models.BooleanField()),
                ('europe_Keymark', models.BooleanField()),
                ('india_QCO', models.BooleanField()),
                ('china', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ScopeStandard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.CharField(max_length=60)),
                ('country', models.CharField(max_length=60)),
                ('scope', models.CharField(max_length=5000)),
            ],
        ),
    ]