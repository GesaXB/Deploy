# Generated by Django 5.1.4 on 2024-12-21 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0002_project_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='category',
            new_name='skills',
        ),
    ]
