# Generated by Django 5.0 on 2024-05-30 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0004_remove_criminalcase_associated_case_files_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criminalcase',
            name='associated_case_files',
        ),
    ]
