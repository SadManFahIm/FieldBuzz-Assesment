# Generated by Django 3.1.2 on 2020-12-10 10:08

import authenticate.validators
import django.core.validators
from django.db import migrations, models
import unixtimestampfield.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tsync_id', models.CharField(blank=True, default=uuid.uuid4, editable=False, max_length=55, unique=True)),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=256)),
                ('phone_number', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'", regex='^\\+?1?\\d{9,14}$')])),
                ('full_address', models.CharField(blank=True, max_length=512, null=True)),
                ('name_of_university', models.CharField(max_length=256)),
                ('graduation_year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2015), django.core.validators.MaxValueValidator(2020)])),
                ('cgpa', models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(2.0), django.core.validators.MaxValueValidator(4.0)])),
                ('experience_in_months', models.PositiveIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('current_work_place_name', models.CharField(blank=True, max_length=256)),
                ('applying_in', models.CharField(choices=[('Mobile', 'Mobile'), ('Backend', 'Backend')], max_length=20)),
                ('expected_salary', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(15000), django.core.validators.MaxValueValidator(60000)])),
                ('field_buzz_reference', models.CharField(blank=True, max_length=256)),
                ('github_project_url', models.URLField(max_length=512)),
                ('cv_file', models.FileField(null=True, upload_to='files/', validators=[authenticate.validators.validate_file], verbose_name='')),
                ('cv_file_tsync_id', models.CharField(blank=True, default=uuid.uuid4, editable=False, max_length=55, unique=True)),
                ('on_spot_update_time', unixtimestampfield.fields.UnixTimeStampField(auto_now=True)),
                ('on_spot_creation_time', unixtimestampfield.fields.UnixTimeStampField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]