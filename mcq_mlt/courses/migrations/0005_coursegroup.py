# Generated by Django 4.0.1 on 2022-04-05 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_email_max_length'),
        ('courses', '0004_usersreadchapters_chapter_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('allow_students', models.BooleanField(default=True)),
                ('modelset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courses.usersreadchapters')),
                ('social_auth_users', models.ManyToManyField(blank=True, to='account.EmailAddress')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
