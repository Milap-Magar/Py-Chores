# Generated by Django 4.0.1 on 2022-03-14 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0021_alter_modelset_minutes_quizgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesyllabus',
            name='image',
            field=models.ImageField(default='/category_image/level1.jpg', upload_to='syllabus_image'),
        ),
    ]
