# Generated by Django 2.0.5 on 2018-07-17 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppCategoryMapings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_primary', models.BooleanField(choices=[('1', 'is_primary'), ('0', 'None')], default=0)),
                ('app_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_category.AppCategories')),
            ],
        ),
        migrations.CreateModel(
            name='AppCoverPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_pic', models.ImageField(default=None, upload_to='cover_pics')),
                ('is_admin', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('app_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_category.AppCategories')),
            ],
        ),
        migrations.CreateModel(
            name='AppImgages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_images', models.ImageField(default=None, upload_to='app_images')),
                ('src', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AppMasters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(blank=True, max_length=100, null=True)),
                ('business_description', models.TextField(blank=True, null=True)),
                ('business_est_year', models.IntegerField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, default=None, null=True, upload_to='logos')),
                ('locality', models.TextField(blank=True, null=True)),
                ('is_physical_store', models.BooleanField(default=True)),
                ('store_address', models.TextField(blank=True, null=True)),
                ('lat', models.CharField(blank=True, max_length=255, null=True)),
                ('long', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_no1', models.BigIntegerField(blank=True, null=True)),
                ('contact_no2', models.BigIntegerField(blank=True, null=True)),
                ('contact_no3', models.BigIntegerField(blank=True, null=True)),
                ('is_always_open', models.BooleanField(choices=[('1', 'is_allose_open'), ('0', 'None')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('app_url', models.CharField(blank=True, max_length=500, null=True)),
                ('visiting_count', models.BigIntegerField(blank=True, default=0, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='appimgages',
            name='appmaster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_masters.AppMasters'),
        ),
        migrations.AddField(
            model_name='appcategorymapings',
            name='appmaster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_masters.AppMasters'),
        ),
    ]
