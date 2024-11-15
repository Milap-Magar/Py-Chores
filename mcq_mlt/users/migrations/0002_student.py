# Generated by Django 4.0.1 on 2022-02-18 11:06

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=255)),
                ('achievement_success', models.CharField(help_text='BMLT 2073 Batch Entrance Topper', max_length=75)),
                ('little_description', ckeditor.fields.RichTextField()),
                ('student_picture', models.ImageField(upload_to='student__image')),
            ],
        ),
    ]
