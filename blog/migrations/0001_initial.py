# Generated by Django 3.2 on 2021-05-05 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('img', models.ImageField(upload_to='blog_img')),
                ('caption', models.CharField(max_length=1000)),
                ('post', models.TextField()),
                ('author', models.CharField(max_length=1000)),
                ('published_date', models.DateTimeField(blank=True)),
            ],
        ),
    ]
