# Generated by Django 4.0.4 on 2022-07-01 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_diet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='diet',
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(default='none', max_length=10),
        ),
    ]
