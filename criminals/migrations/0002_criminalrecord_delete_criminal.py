# Generated by Django 5.0 on 2024-05-29 15:14

import criminals.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0001_initial'),
        ('officers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CriminalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('date_of_arrest', models.DateField(auto_now_add=True)),
                ('time_of_arrest', models.TimeField(auto_now_add=True)),
                ('tribe', models.CharField(max_length=100)),
                ('religion', models.CharField(max_length=100)),
                ('marital_status', models.CharField(max_length=100)),
                ('height_in_meters', models.FloatField()),
                ('weight_in_kg', models.FloatField()),
                ('gender', models.CharField(max_length=10)),
                ('nin', models.CharField(max_length=100, unique=True)),
                ('address', models.TextField()),
                ('contact_info', models.CharField(max_length=100)),
                ('distinctive_features', models.TextField(default='Scars, Tribal marks, Tattoos, Piercings, etc.')),
                ('next_of_kin', models.CharField(max_length=255)),
                ('finger_print', models.ImageField(blank=True, upload_to='images/')),
                ('mugshot', models.ImageField(blank=True, upload_to='images/')),
                ('known_aliases', models.CharField(max_length=255)),
                ('associates', models.CharField(blank=True, max_length=255)),
                ('case_number', models.CharField(default=criminals.models.generate_case_number, max_length=9, unique=True)),
                ('arresting_officer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='officers.officer')),
            ],
        ),
        migrations.DeleteModel(
            name='Criminal',
        ),
    ]
