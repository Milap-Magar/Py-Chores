# Generated by Django 4.0.1 on 2022-02-18 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_category_category_image_alter_course_level_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='syllabus',
            name='syllabus_image',
            field=models.ImageField(default='/syllabus_image/syllabus1.jpg', upload_to='syllabus_image'),
        ),
    ]
