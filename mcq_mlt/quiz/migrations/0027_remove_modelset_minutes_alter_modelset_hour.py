# Generated by Django 4.0.1 on 2022-03-26 05:36

from django.db import migrations, models
import mcq_mlt.validators


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0026_quizgroup_allow_students'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelset',
            name='minutes',
        ),
        migrations.AlterField(
            model_name='modelset',
            name='hour',
            field=models.CharField(default='01', help_text='write 01, 02, or 03 like numbers only', max_length=75, validators=[mcq_mlt.validators.validate_time]),
        ),
    ]
