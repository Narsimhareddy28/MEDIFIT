# Generated by Django 4.0.3 on 2022-04-22 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_emailid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='emailId',
            field=models.EmailField(default='', max_length=256),
        ),
    ]
