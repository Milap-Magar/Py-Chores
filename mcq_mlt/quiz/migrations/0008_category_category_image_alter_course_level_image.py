# Generated by Django 4.0.1 on 2022-02-18 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_course_level_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(default='/category_image/level1.jpg', upload_to='category_image'),
        ),
        migrations.AlterField(
            model_name='course',
            name='level_image',
            field=models.ImageField(default='/level_image/level1.jpg', upload_to='level_image'),
        ),
    ]
