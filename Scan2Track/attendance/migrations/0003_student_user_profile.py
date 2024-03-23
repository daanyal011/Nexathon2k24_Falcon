# Generated by Django 5.0.3 on 2024-03-23 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_rename_date_attendance_attendance_date_and_more'),
        ('users', '0002_userprofile_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='user_profile',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to='users.userprofile'),
            preserve_default=False,
        ),
    ]