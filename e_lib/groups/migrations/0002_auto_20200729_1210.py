# Generated by Django 2.2 on 2020-07-29 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='sem_no',
            field=models.CharField(default=['Semester 1'], max_length=128, unique=True),
        ),
    ]
