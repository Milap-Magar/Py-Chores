# Generated by Django 4.0.1 on 2022-02-18 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_questions_explanation'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='level_image',
            field=models.ImageField(default='level1.jpg', upload_to='level_image'),
        ),
    ]
