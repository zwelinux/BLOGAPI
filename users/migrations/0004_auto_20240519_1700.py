# Generated by Django 2.2.6 on 2024-05-19 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20240519_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_pics/user.png', upload_to='profile_pics'),
        ),
    ]