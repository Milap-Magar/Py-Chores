# Generated by Django 4.0.1 on 2022-03-04 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0012_coursesyllabus_remove_syllabus_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='syllabus',
            name='syllabus_for',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz.coursesyllabus'),
            preserve_default=False,
        ),
    ]