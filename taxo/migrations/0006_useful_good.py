# Generated by Django 4.2.3 on 2024-01-06 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxo', '0005_useful_delete_ideapic'),
    ]

    operations = [
        migrations.AddField(
            model_name='useful',
            name='good',
            field=models.ImageField(default=0, upload_to='check'),
            preserve_default=False,
        ),
    ]