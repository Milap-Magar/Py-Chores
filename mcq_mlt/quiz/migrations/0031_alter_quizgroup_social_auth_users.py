# Generated by Django 4.0.1 on 2022-04-03 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_email_max_length'),
        ('quiz', '0030_alter_quizgroup_social_auth_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizgroup',
            name='social_auth_users',
            field=models.ManyToManyField(blank=True, to='account.EmailAddress'),
        ),
    ]
