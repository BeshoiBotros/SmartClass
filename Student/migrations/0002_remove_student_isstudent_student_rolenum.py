# Generated by Django 4.2.1 on 2023-05-15 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='isStudent',
        ),
        migrations.AddField(
            model_name='student',
            name='roleNum',
            field=models.IntegerField(default=2),
        ),
    ]
