# Generated by Django 2.2 on 2019-08-08 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='introduction',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
