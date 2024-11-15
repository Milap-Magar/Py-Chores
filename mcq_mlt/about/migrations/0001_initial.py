# Generated by Django 4.0.1 on 2022-02-17 08:23

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_mcqmlt', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Advisors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('designation', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('designation', models.CharField(max_length=225)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='team_images')),
            ],
        ),
    ]