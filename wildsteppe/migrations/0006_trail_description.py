# Generated by Django 4.2 on 2023-04-18 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wildsteppe', '0005_alter_customuser_options_remove_customuser_birthday_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trail',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
