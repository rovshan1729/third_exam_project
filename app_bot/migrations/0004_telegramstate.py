# Generated by Django 4.0.6 on 2022-07-14 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_bot', '0003_telegramuser_phone_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scenario', models.CharField(max_length=30)),
                ('step', models.CharField(max_length=30)),
                ('context', models.JSONField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_bot.telegramuser')),
            ],
        ),
    ]