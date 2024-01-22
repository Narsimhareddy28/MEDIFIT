# Generated by Django 4.0.3 on 2022-04-08 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('problems', models.ManyToManyField(to='problems.problems')),
            ],
        ),
    ]
