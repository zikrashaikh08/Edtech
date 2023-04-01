# Generated by Django 4.1.1 on 2023-04-01 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eLearning', '0021_coursequiz_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttempQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eLearning.quizquestions')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eLearning.student')),
            ],
            options={
                'verbose_name_plural': '95. Attempted Questions',
            },
        ),
    ]
