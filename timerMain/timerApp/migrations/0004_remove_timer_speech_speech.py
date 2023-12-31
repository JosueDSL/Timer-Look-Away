# Generated by Django 5.0 on 2023-12-16 03:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timerApp', '0003_rename_greeting_timer_speech'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timer',
            name='speech',
        ),
        migrations.CreateModel(
            name='Speech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('message', models.CharField(max_length=128)),
                ('date', models.DateField(auto_now_add=True)),
                ('timer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timerApp.timer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speeches', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
