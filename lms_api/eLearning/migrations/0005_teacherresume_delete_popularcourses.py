# Generated by Django 4.1.1 on 2022-11-03 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eLearning', '0004_popularcourses'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherResume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eLearning.teacher')),
            ],
            options={
                'verbose_name_plural': 'Teacher Resume',
            },
        ),
        migrations.DeleteModel(
            name='PopularCourses',
        ),
    ]
