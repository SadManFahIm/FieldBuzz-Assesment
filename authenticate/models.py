from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
import uuid
from unixtimestampfield.fields import UnixTimeStampField
from django.core.validators import RegexValidator

from .validators import validate_file
# Create your models here.

application_choice_field = [
    ("Mobile", "Mobile"),
    ("Backend", "Backend"),
]

class Person(models.Model):
    tsync_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=55)
    name = models.CharField(max_length=256, blank=False)
    email = models.EmailField(max_length=256, blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$', message="Phone number must be entered in the format: '+999999999'")
    phone_number = models.CharField(validators=[phone_regex], max_length=14, blank=False)
    full_address = models.CharField(max_length=512, null=True, blank=True)
    name_of_university = models.CharField(max_length=256, blank=False)
    graduation_year = models.PositiveIntegerField(validators=[MinValueValidator(2015),
                                       MaxValueValidator(2020)], blank=False)
    cgpa = models.FloatField(validators=[MinValueValidator(2.0),
                                       MaxValueValidator(4.0)], blank=True)
    experience_in_months = models.PositiveIntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(100)], blank=True)
    current_work_place_name = models.CharField(max_length=256, blank=True)
    applying_in = models.CharField(choices=application_choice_field, blank=False, max_length=20)
    expected_salary = models.PositiveIntegerField(validators=[MinValueValidator(15000),
                                       MaxValueValidator(60000)], blank=False)
    field_buzz_reference = models.CharField(max_length=256, blank=True)
    github_project_url = models.URLField(max_length=512, blank=False)

    cv_file = models.FileField(upload_to='files/', null=True, blank=False, verbose_name="", validators=[validate_file])
    cv_file_tsync_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, max_length=55)
    on_spot_update_time = UnixTimeStampField(auto_now=True)
    on_spot_creation_time = UnixTimeStampField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
