# Generated by Django 4.0.1 on 2022-03-06 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0014_alter_coursesyllabus_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syllabus',
            name='syllabus_for',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='quiz.coursesyllabus'),
        ),
    ]