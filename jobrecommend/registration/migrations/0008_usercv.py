# Generated by Django 3.0.8 on 2021-05-25 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_auto_20210512_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='usercv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('cv', models.FileField(upload_to='')),
            ],
        ),
    ]