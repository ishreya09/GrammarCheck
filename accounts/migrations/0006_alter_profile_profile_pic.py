# Generated by Django 3.2 on 2021-05-09 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210509_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Profile_pic',
            field=models.ImageField(blank=True, default='user_dp/default.png', null=True, upload_to='user_dp'),
        ),
    ]
