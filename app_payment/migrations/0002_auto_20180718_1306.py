# Generated by Django 2.0.5 on 2018-07-18 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apppayment',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
