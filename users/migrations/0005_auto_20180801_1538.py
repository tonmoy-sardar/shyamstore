# Generated by Django 2.0.5 on 2018-08-01 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userdetails_otm_send_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='otm_send_time',
            new_name='otp_send_time',
        ),
    ]
