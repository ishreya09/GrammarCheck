# Generated by Django 3.2 on 2021-05-09 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Profile_pic',
            field=models.ImageField(blank=True, default='user_dp/default.png', null=True, upload_to='user_dp'),
        ),
    ]
