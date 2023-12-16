# Generated by Django 5.0 on 2023-12-16 04:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timerApp', '0004_remove_timer_speech_speech'),
    ]

    operations = [
        migrations.AddField(
            model_name='timer',
            name='message',
            field=models.CharField(default=django.utils.timezone.now, max_length=128),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Speech',
        ),
    ]
