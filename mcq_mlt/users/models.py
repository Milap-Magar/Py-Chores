import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class User(AbstractUser):
    qualification_choice = (
        ("LA", "Lab Assistance"),
        ("LT", "Lab Technician"),
        ("BMLT", "B. MLT"),
        ("MMLT", "MSc. MLT")
    )

    gender_choice = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'OTher'),
    )
    # customizing fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(verbose_name='email',
                              max_length=100, unique=True)
    gender = models.CharField(max_length=1, choices=gender_choice)
    qualification = models.CharField(
        max_length=6, choices=qualification_choice)
    phonenumber = PhoneNumberField()
    is_EDUMLT_student = models.BooleanField(default=False)
    student_code = models.CharField(max_length=6, blank=True, default='')
    heard_from = models.CharField(max_length=50, blank=True, default='')

    USERNAME_FIELD = 'email'  # now user can log in using email
    # here, email is already a required field
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email



''' Students success story model '''
class Student(models.Model):
    student_name = models.CharField(max_length=255)
    achievement_success = models.CharField(max_length=75, help_text='BMLT 2073 Batch Entrance Topper')
    little_description = RichTextField()
    student_picture = models.ImageField(upload_to='student__image')


    def __str__(self):
        return self.student_name
