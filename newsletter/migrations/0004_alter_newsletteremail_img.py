# Generated by Django 3.2 on 2021-05-10 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_newsletteremail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletteremail',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='newsletters'),
        ),
    ]