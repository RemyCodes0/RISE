# Generated by Django 4.2.3 on 2024-01-05 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxo', '0003_alter_question_options_question_know'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdeaPic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea', models.ImageField(upload_to='')),
            ],
        ),
    ]
