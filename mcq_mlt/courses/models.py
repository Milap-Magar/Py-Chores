from django.db import models
from allauth.account.models import EmailAddress

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import CharField
from users.models import User


class Subjects(models.Model):
    name =models.CharField(max_length=50)
    description = RichTextField(null=True)
    image = models.ImageField(upload_to='subject_image', default='/courses/level1.jpg')
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
       

class Units(models.Model):
    subject=models.ForeignKey(Subjects, on_delete=models.CASCADE)
    name=models.CharField(max_length=75, help_text="Enter the unit name in the format: Unit -1 : Bacteriology")
    description=RichTextUploadingField(null=True)

    def __str__(self):
        return self.name


class Chapters(models.Model):
    subject=models.ForeignKey(Subjects, on_delete=models.CASCADE)
    unit=models.ForeignKey(Units, on_delete=models.CASCADE)
    name=models.CharField(max_length=75)
    content=RichTextUploadingField()
    mark_as_read=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


''' This models links the users who have read a particular chapter  '''

class UsersReadChapters(models.Model):
    chapter_name = models.CharField(max_length = 255, default="Default")
    unit = models.ForeignKey(Units,on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapters, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.chapter_name


class ChapterWiseModelset(models.Model):
    modelset_title = models.CharField(max_length=75, help_text='Give a name to it')
    chapter = models.ForeignKey(Chapters, on_delete=models.CASCADE)

    def __str__(self):
        return self.modelset_title


class Questions(models.Model):
    answer_choices=[
        ('option1','option1'),
        ('option2','option2'),
        ('option3','option3'),
        ('option4','option4'),
    ]
    modelset = models.ForeignKey(ChapterWiseModelset, on_delete=models.CASCADE)
    question_statement = RichTextField()
    choice_1 = RichTextField()
    choice_2 = RichTextField()
    choice_3 = RichTextField()
    choice_4 = RichTextField()
    answer = models.CharField(max_length=75, choices=answer_choices, default='option1')
    explanation = RichTextField(blank=True)
    
    def __str__(self):
        return '{}'.format(self.question_statement)

class SubjectGroup(models.Model):
    """ allow the users with in model only to access the quiz once """
    name = models.CharField(max_length=50)
    subject = models.OneToOneField(Subjects, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)
    social_auth_users = models.ManyToManyField(EmailAddress, blank=True)
    allow_students = models.BooleanField(default= True)

    def __str__(self):
        return self.name

    def get_users(self):
        return self.users.all()
