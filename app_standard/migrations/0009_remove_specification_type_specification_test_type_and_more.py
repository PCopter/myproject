# Generated by Django 5.0.4 on 2024-07-10 07:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_standard', '0008_alter_countryspecification_relatemark'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specification',
            name='type',
        ),
        migrations.AddField(
            model_name='specification',
            name='test_type',
            field=models.CharField(choices=[('S', 'Sampling test'), ('R', 'Routine test')], default='R', max_length=1),
        ),
        migrations.AlterField(
            model_name='itemtest',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='specification',
            name='description',
            field=models.TextField(default='xxxxxxx', max_length=500),
        ),
        migrations.CreateModel(
            name='CountryTestRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requirement', models.CharField(choices=[('-', 'No requirement'), ('1', 'Should be tested (If possible)'), ('2', 'Std.requirement (Must be tested)'), ('3', 'Std.requirement must be tested at external lab (CCC)'), ('4', 'Std.requirement which can select testing (Between Pressure and Refri. leakage test) (QCO)')], max_length=1)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_standard.country')),
                ('specification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_standard.specification')),
            ],
            options={
                'unique_together': {('country', 'specification')},
            },
        ),
        migrations.DeleteModel(
            name='CountrySpecification',
        ),
    ]