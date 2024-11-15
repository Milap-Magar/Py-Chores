from random import randint
from django.db import models
from ckeditor.fields import RichTextField

from django.db import models

from users.models import User


class About(models.Model):
    about_mcqmlt = RichTextField()
    
    def __str__(self):
        return self.about_mcqmlt


class Team(models.Model):
    name = models.CharField(max_length=225)
    designation = models.CharField(max_length=225)
    picture = models.ImageField(
        upload_to='team_images', blank=True, null=True, help_text='Please insert the image of same sizes for all team members so that it looks good in the frontend of the website.')

    def __str__(self):
        return str(self.name)


class Advisors(models.Model):
    name = models.CharField(max_length=225)
    designation = models.CharField(max_length=225)
    advisor_index = models.IntegerField(
        unique=False,
        help_text='give advisor an index, advisor with highest index will be displayed first.'
    )

    def __str__(self):
        return str(self.name)
