# Generated by Django 4.1.1 on 2023-03-19 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eLearning', '0016_alter_notification_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='notif_subject',
            field=models.CharField(max_length=200, null=True, verbose_name='Notification Subject'),
        ),
    ]
