# Generated by Django 3.0.8 on 2021-05-25 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_usercv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercv',
            name='cv',
            field=models.FileField(upload_to='cv/'),
        ),
    ]
