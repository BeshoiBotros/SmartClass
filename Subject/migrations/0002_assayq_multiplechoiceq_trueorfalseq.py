# Generated by Django 4.2.1 on 2023-05-16 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsSayQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MultipleChoiceQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quistion', models.TextField(max_length=255)),
                ('choiceA', models.TextField(max_length=255)),
                ('choiceB', models.TextField(max_length=255)),
                ('choiceC', models.TextField(max_length=255)),
                ('choiceD', models.TextField(max_length=255)),
                ('answer', models.TextField(choices=[('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd')], default='a')),
                ('degree', models.FloatField(default=0.0, max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='TrueOrFalseQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quistion', models.TextField(max_length=255)),
                ('answer', models.BooleanField()),
            ],
        ),
    ]
