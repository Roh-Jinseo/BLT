# Generated by Django 4.2.8 on 2024-05-22 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='profile_img',
            new_name='img',
        ),
    ]
