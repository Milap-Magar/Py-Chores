from distutils.command.upload import upload
from email.policy import default
from random import choices
from django.db import models
from ckeditor.fields import RichTextField
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _

from mcq_mlt.utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.db import models
from allauth.account.models import EmailAddress

from users.models import User
from mcq_mlt.validators import validate_time, validate_weightage


''' List of courses available : e.g. Lab Assistant, CMLT, BMLT '''
class Course(models.Model):
    course_name = models.CharField(max_length=75, help_text='Enter the course name like: Lab Assistant, CMLT, BMLT')
    course_description = RichTextField()
    level_image = models.ImageField(upload_to='level_image', default='/level_image/level1.jpg')
    slug = models.SlugField(unique=True, default='', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = _("Level")
        verbose_name_plural = _("Levels")

def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender = Course)


class CourseSyllabus(models.Model):
    """
    model for syllabus course
    """
    name = models.CharField(max_length=75, help_text='Enter the course name like: Loksewa - Province I')
    description = RichTextField(null=True)
    image = models.ImageField(upload_to='syllabus_image', default='/category_image/level1.jpg')

    def __str__(self):
        return self.name


''' Syllabus Model '''
class Syllabus(models.Model):
    syllabus_for = models.ForeignKey(CourseSyllabus, on_delete=models.CASCADE)
    syllabus_title = models.CharField(max_length=75, help_text='Enter the syllabus name like: Loksewa Syllabus - Province I')
    syllabus_description = RichTextField(null=True)
    syllabus = models.FileField(upload_to='syllabus_files')

    def __str__(self):
        return self.syllabus_title


''' List of categories available : e.g. Loksewa, License, Entrance '''

class Category(models.Model):
    category_name = models.CharField(max_length=75, help_text='Enter the category name like: Loksewa, License, Entrance')
    category_description = RichTextField()
    category_image = models.ImageField(upload_to='category_image', default='/category_image/level1.jpg')

    course = models.ForeignKey(Course, on_delete=models.CASCADE)


    def __str__(self):
        return self.category_name


# ''' List of Levels available : e.g. Assistant, Technician, Bachelor, Master '''

# class Level(models.Model):
#     level_name = models.CharField(max_length=75, help_text='Enter the level name like: Assistant, Technician, Bachelor, Master')
#     level_description = RichTextField()
#     course = models.ForeignKey(Course, on_delete = models.CASCADE)
#     category = models.ForeignKey(Category, on_delete = models.CASCADE)

#     def __str__(self):
        
#         return '{} {} {}'.format(self.level_name, self.course, self.category)


''' List of question model sets : e.g. Modelset January 27th, Modelset Feb 5th '''

class Modelset(models.Model):
    modelset_title = models.CharField(max_length=75, help_text='Enter the Modelset name like: February First Week - BMLT Assistant Entrance')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # level = models.ForeignKey(Level, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    free = models.BooleanField(default=False)
    weightage = models.IntegerField(
        help_text='give questions of this modelset a point.',
        validators=[validate_weightage]
    )
    hour = models.CharField(max_length=75,
        help_text='write 01, 02, or 03 like numbers only',
        default='01',
        validators=[validate_time]
    )
    minutes= models.CharField(max_length=75, help_text='write 01, 02, or 03 like numbers only', default='00')

    def __str__(self):
        return '{} {} {}'.format(self.modelset_title, self.course, self.category)


''' List of questions for a particular modelset '''

class Questions(models.Model):
    answer_choices=[
        ('option1','option1'),
        ('option2','option2'),
        ('option3','option3'),
        ('option4','option4'),
    ]
    modelset = models.ForeignKey(Modelset, on_delete=models.CASCADE)
    question_statement = RichTextField()
    choice_1 = RichTextField()
    choice_2 = RichTextField()
    choice_3 = RichTextField()
    choice_4 = RichTextField()
    answer = models.CharField(max_length=75, choices=answer_choices, default='option1')
    # explanation = RichTextField(default='')
    explanation = RichTextField(blank=True)
    
    def __str__(self):
        return '{}'.format(self.question_statement)


''' Question of the Day model '''
class QOTD(models.Model):
    answer_choices=[
            ('option1','option1'),
            ('option2','option2'),
            ('option3','option3'),
            ('option4','option4'),
        ]

    qotd_statement = RichTextField()
    op_1 = RichTextField(default='')
    op_2 = RichTextField(default='')
    op_3 = RichTextField(default='')
    op_4 = RichTextField(default='')
    answer = models.CharField(max_length=75, choices=answer_choices, default='option1')
    explanation = RichTextField(blank=True)

    
    def __str__(self):
        return '{}'.format(self.qotd_statement)


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    modelset = models.ForeignKey(Modelset, on_delete=models.CASCADE)
    markes_obtained = models.IntegerField()
    correct = models.IntegerField(null=True)
    wrong = models.IntegerField(null=True)
    unanswered = models.IntegerField(null=True)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Result of  {} {}'.format(self.user.first_name, self.user.last_name)



""" allow the users with in the student group to access the quiz"""
class StudentGroup(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    def get_users(self):
        return self.users.all()


class QuizGroup(models.Model):
    """ allow the users with in model only to access the quiz once """
    name = models.CharField(max_length=50)
    modelset = models.OneToOneField(Modelset, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)
    social_auth_users = models.ManyToManyField(EmailAddress, blank=True)
    allow_students = models.BooleanField(default= True)

    def __str__(self):
        return self.name

    def get_users(self):
        return self.users.all()
