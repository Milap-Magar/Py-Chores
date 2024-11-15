# Generated by Django 4.0.1 on 2022-03-26 05:58

from django.db import migrations, models
import mcq_mlt.validators


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0027_remove_modelset_minutes_alter_modelset_hour'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelset',
            name='minutes',
            field=models.CharField(default='00', help_text='write 01, 02, or 03 like numbers only', max_length=75),
        ),
        migrations.AlterField(
            model_name='modelset',
            name='hour',
            field=models.CharField(default='01', help_text='write 01, 02, or 03 like numbers only', max_length=75, validators=[mcq_mlt.validators.validate_time]),
        ),
    ]