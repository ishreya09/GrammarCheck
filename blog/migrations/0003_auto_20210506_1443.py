# Generated by Django 3.2 on 2021-05-06 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210505_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogger',
            name='caption',
        ),
        migrations.RemoveField(
            model_name='blogger',
            name='img',
        ),
        migrations.RemoveField(
            model_name='blogger',
            name='post',
        ),
        migrations.AddField(
            model_name='blogger',
            name='caption1',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='caption10',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='caption11',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='caption12',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='caption13',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='caption14',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='caption15',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='caption2',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='caption3',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='caption4',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='caption5',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='caption6',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='caption7',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='caption8',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='caption9',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='category',
            field=models.IntegerField(choices=[(0, 'Uncategorised'), (1, 'GrammarRules'), (2, 'FunwithGrammar'), (3, 'ExercisesofGrammar'), (4, 'Essays'), (5, 'Letters'), (6, 'Quotes'), (7, 'Articles'), (8, 'Poems'), (9, 'Short Stories'), (10, 'Other topics')], default=0),
        ),
        migrations.AddField(
            model_name='blogger',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='blog_img'),
        ),
        migrations.AddField(
            model_name='blogger',
            name='img10',
            field=models.ImageField(blank=True, null=True, upload_to='blog_img'),
        ),
        migrations.AddField(
            model_name='blogger',
            name='img11',
            field=models.ImageField(blank=True, null=True, upload_to='blog_img'),
        ),
        migrations.AddField(
            model_name='blogger',
            name='img12',
            field=models.ImageField(blank=True, null=True, upload_to='blog_img'),
        ),
        migrations.AddField(
            model_name='blogger',
            name='img13',
            field=models.ImageField(blank=True, null=True, upload_to='blog_img'),
        ),
        migrations.AddField(
            model_name='blogger',
            name='img14',
            field=models.ImageField(blank=True, null=True, upload_to='blog_img'),
        ),
        migrations.AddField(
            model_name='blogger',
            name='img15',
            field=models.ImageField(blank=True, null=True, upload_to='blog_img'),
        ),
        migrations.AddField(
            model_name='blogger',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='blog_img'),
        ),
        migrations.AddField(
            model_name='blogger',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='blog_img'),
        ),
        migrations.AddField(
            model_name='blogger',
            name='img4',
            field=models.ImageField(blank=True, null=True, upload_to='blog_img'),
        ),
        migrations.AddField(
            model_name='blogger',
            name='img5',
            field=models.ImageField(blank=True, null=True, upload_to='blog_img'),
        ),
        migrations.AddField(
            model_name='blogger',
            name='img6',
            field=models.ImageField(blank=True, null=True, upload_to='blog_img'),
        ),
        migrations.AddField(
            model_name='blogger',
            name='img7',
            field=models.ImageField(blank=True, null=True, upload_to='blog_img'),
        ),
        migrations.AddField(
            model_name='blogger',
            name='img8',
            field=models.ImageField(blank=True, null=True, upload_to='blog_img'),
        ),
        migrations.AddField(
            model_name='blogger',
            name='img9',
            field=models.ImageField(blank=True, null=True, upload_to='blog_img'),
        ),
        migrations.AddField(
            model_name='blogger',
            name='post1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='post10',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='post11',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='post12',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='post13',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='post14',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='post15',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='post2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='post3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='post4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='post5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='post6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='post7',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='post8',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='post9',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='subheading1',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='subheading10',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='subheading11',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='subheading12',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='subheading13',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='subheading14',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='subheading15',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='subheading2',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='subheading3',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='subheading4',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='subheading5',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='subheading6',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='subheading7',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='subheading8',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='subheading9',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
