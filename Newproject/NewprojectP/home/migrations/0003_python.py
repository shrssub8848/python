# Generated by Django 2.2 on 2019-08-08 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190808_0622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Python',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Session', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]
