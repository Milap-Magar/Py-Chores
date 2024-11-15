# Generated by Django 4.0.1 on 2022-02-17 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='picture',
            field=models.ImageField(blank=True, help_text='Please insert the image of same sizes for all team members so that it looks good in the frontend of the website.', null=True, upload_to='team_images'),
        ),
    ]
