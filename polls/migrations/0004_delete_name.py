# Generated by Django 3.2 on 2022-12-16 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_rename_age_name_ages'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Name',
        ),
    ]
