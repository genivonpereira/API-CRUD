# Generated by Django 5.0.6 on 2024-05-22 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0002_rename_user_nickname_user_user_nickname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_Nickname',
            new_name='user_nickname',
        ),
    ]