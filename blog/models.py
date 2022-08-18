from django.db import models
import django.utils.timezone 
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish"),
    (2, "Delete")
)

CATEGORY= (
    (0,"Uncategorised"),
    (1,"GrammarRules"),
    (2,"FunwithGrammar"),
    (3,"ExercisesofGrammar"),
    (4,"Essays"),
    (5,"Letters"),
    (6,"Quotes"),
    (7, "Articles"),
    (8,"Poems"),
    (9,"Short Stories"),
    (10,"Other topics")
)

class Blogger(models.Model):
    title = models.CharField(max_length=1000)
    # slug field auto populated using title with unique constraint
    slug = models.SlugField(max_length=200, unique=True)
    subheading1 =models.CharField(max_length=1000,null=True, blank=True)
    img1 = models.ImageField(upload_to = 'blog_img',null=True, blank=True)
    caption1 =models.CharField(max_length=1000,null=True, blank=True)
    post1 = models.TextField(null=True, blank=True)
    subheading2 =models.CharField(max_length=1000,null=True, blank=True)
    img2 = models.ImageField(upload_to = 'blog_img',null=True, blank=True)
    caption2 =models.CharField(max_length=1000,null=True, blank=True)
    post2 = models.TextField(null=True, blank=True)
    subheading3 =models.CharField(max_length=1000,null=True, blank=True)
    img3 = models.ImageField(upload_to = 'blog_img',null=True, blank=True)
    caption3 =models.CharField(max_length=1000,null=True, blank=True)
    post3 = models.TextField(null=True, blank=True)
    subheading4 =models.CharField(max_length=1000,null=True, blank=True)
    img4 = models.ImageField(upload_to = 'blog_img',null=True, blank=True)
    caption4 =models.CharField(max_length=1000,null=True, blank=True)
    post4 = models.TextField(null=True, blank=True)
    subheading5 =models.CharField(max_length=1000,null=True, blank=True)
    img5 = models.ImageField(upload_to = 'blog_img',null=True, blank=True)
    caption5 =models.CharField(max_length=1000,null=True, blank=True)
    post5 = models.TextField(null=True, blank=True)
    subheading6 =models.CharField(max_length=1000,null=True, blank=True)
    img6 = models.ImageField(upload_to = 'blog_img',null=True, blank=True)
    caption6 =models.CharField(max_length=1000,null=True, blank=True)
    post6 = models.TextField(null=True, blank=True)
    subheading7 =models.CharField(max_length=1000,null=True, blank=True)
    img7 = models.ImageField(upload_to = 'blog_img',null=True, blank=True)
    caption7 =models.CharField(max_length=1000,null=True, blank=True)
    post7 = models.TextField(null=True, blank=True)
    subheading8 =models.CharField(max_length=1000,null=True, blank=True)
    img8 = models.ImageField(upload_to = 'blog_img',null=True, blank=True)
    caption8 =models.CharField(max_length=1000,null=True, blank=True)
    post8 = models.TextField(null=True, blank=True)
    subheading9 =models.CharField(max_length=1000,null=True, blank=True)
    img9 = models.ImageField(upload_to = 'blog_img',null=True, blank=True)
    caption9 =models.CharField(max_length=1000,null=True, blank=True)
    post9 = models.TextField(null=True, blank=True)
    subheading10 =models.CharField(max_length=1000,null=True, blank=True)
    img10 = models.ImageField(upload_to = 'blog_img',null=True, blank=True)
    caption10 =models.CharField(max_length=1000,null=True, blank=True)
    post10 = models.TextField(null=True, blank=True)
    subheading11 =models.CharField(max_length=1000,null=True, blank=True)
    img11 = models.ImageField(upload_to = 'blog_img',null=True, blank=True)
    caption11 =models.CharField(max_length=1000,null=True, blank=True)
    post11 = models.TextField(null=True, blank=True)
    subheading12 =models.CharField(max_length=1000,null=True, blank=True)
    img12 = models.ImageField(upload_to = 'blog_img',null=True, blank=True)
    caption12 =models.CharField(max_length=1000,null=True, blank=True)
    post12 = models.TextField(null=True, blank=True)
    subheading13 =models.CharField(max_length=1000,null=True, blank=True)
    img13 = models.ImageField(upload_to = 'blog_img',null=True, blank=True)
    caption13 =models.CharField(max_length=1000,null=True, blank=True)
    post13 = models.TextField(null=True, blank=True)
    subheading14 =models.CharField(max_length=1000,null=True, blank=True)
    img14 = models.ImageField(upload_to = 'blog_img',null=True, blank=True)
    caption14 =models.CharField(max_length=1000,null=True, blank=True)
    post14 = models.TextField(null=True, blank=True)
    subheading15 =models.CharField(max_length=1000,null=True, blank=True)
    img15 = models.ImageField(upload_to = 'blog_img',null=True, blank=True)
    caption15 =models.CharField(max_length=1000,null=True, blank=True)
    post15 = models.TextField(null=True, blank=True)
    # meta descrption for SEO benifits
    metades = models.CharField(max_length=300, default="new post")
    # status of post
    status = models.IntegerField(choices=STATUS, default=0)
    category=models.IntegerField(choices=CATEGORY,default= 0 )
    author = models.CharField(max_length=1000)
    published_date = models.DateTimeField(blank=True)
     # and date time fields automatically populated using system time
    updated_on = models.DateTimeField(auto_now= True)
    # meta for the class
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
   