# Generated by Django 3.2.12 on 2024-02-29 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_rename_analyst_user_id_analysis_analyst_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='analysis',
            old_name='id',
            new_name='analysis_id',
        ),
    ]