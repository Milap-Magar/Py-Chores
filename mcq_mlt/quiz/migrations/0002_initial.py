# Generated by Django 4.0.1 on 2022-02-11 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='questions',
            name='modelset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.modelset'),
        ),
        migrations.AddField(
            model_name='modelset',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.category'),
        ),
        migrations.AddField(
            model_name='modelset',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.course'),
        ),
        migrations.AddField(
            model_name='category',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.course'),
        ),
    ]
