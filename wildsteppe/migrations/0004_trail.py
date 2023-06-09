# Generated by Django 4.2 on 2023-04-18 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wildsteppe', '0003_activity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('distance', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('image', models.URLField()),
                ('pets_allowed', models.BooleanField()),
            ],
        ),
    ]
