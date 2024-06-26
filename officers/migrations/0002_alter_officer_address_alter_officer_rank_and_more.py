# Generated by Django 5.0 on 2024-05-29 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officer',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='officer',
            name='rank',
            field=models.CharField(choices=[('Recruit Constable', 'Recruit Constable'), ('Constable', 'Constable'), ('Corporal', 'Corporal'), ('Sergeant', 'Sergeant'), ('Sergeant Major', 'Major'), ('Inspector', 'Inspector')], max_length=100),
        ),
        migrations.AlterField(
            model_name='officer',
            name='sex',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='Male', max_length=10),
        ),
    ]
