# Generated by Django 4.2.3 on 2024-01-04 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxo', '0002_remove_question_finish_valid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['level']},
        ),
        migrations.AddField(
            model_name='question',
            name='know',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
