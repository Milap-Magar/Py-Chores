# Generated by Django 4.0.1 on 2022-03-06 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0016_alter_syllabus_syllabus_for'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syllabus',
            name='syllabus_for',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.coursesyllabus'),
        ),
    ]
