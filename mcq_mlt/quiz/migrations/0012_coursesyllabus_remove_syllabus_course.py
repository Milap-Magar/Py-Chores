# Generated by Django 4.0.1 on 2022-03-04 11:32

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_alter_questions_explanation'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseSyllabus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the course name like: Loksewa - Province I', max_length=75)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='syllabus',
            name='course',
        ),
    ]
