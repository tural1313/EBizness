from django.db import models
from tinymce.models import HTMLField


class Banner(models.Model):
    image = models.ImageField(upload_to="banner_image/")
    title = models.CharField(max_length=200)
    content =models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title

    
class OurService(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
class Statistic(models.Model):
    percentage = models.IntegerField(default=0)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories" 


    def __str__(self):
        return self.title
    
class Portfolio(models.Model):
    category = models.ManyToManyField(Category, blank=True) 
    image = models.ImageField(upload_to='portfolio_images/')
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField() 
    
    def __str__(self):
        return self.question
    
class Section(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    content2 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class Team(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='team_images/')
    profession = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class SocialMedia(models.Model):
    icon = models.CharField(max_length=50)
    link = models.URLField(max_length=256)
    team = models.ForeignKey(Team, models.CASCADE, related_name='socialmedias')

    def __str__(self):
        return self.icon

class PricingTable(models.Model):
    packname = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    label = models.CharField(max_length=20, blank=True, null=True)
    online_system = models.BooleanField(default=True)
    full_access = models.BooleanField(default=True)
    free_apps = models.BooleanField(default=True)
    multiple_slider = models.BooleanField(default=True)
    free_domin = models.BooleanField(default=True)
    support_unlimited = models.BooleanField(default=True)
    payment_online = models.BooleanField(default=True)
    cash_back = models.BooleanField(default=True)

    def __str__(self):
        return self.packname

class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.name
    
class SiteSettings(models.Model):
    logo = models.ImageField(upload_to="site_images/", blank=True, null=True)
    about_image = models.ImageField(upload_to="site_images/", blank=True, null=True)
    about_content = models.TextField(blank=True, null=True)
    about_title = models.CharField(max_length=50,blank=True, null=True)
    middle_image = models.ImageField(upload_to="site_images/", blank=True, null=True)
    middle_title = models.CharField(max_length=200, blank=True, null=True)
    middle_content = models.TextField(blank=True, null=True)
    ct_phone = models.IntegerField(blank=True, null=True)
    working_shift = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField(max_length=256,blank=True, null=True)
    website = models.URLField(max_length=256,blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    location2 = models.TextField(blank=True, null=True)
    end_content = models.TextField(blank=True, null=True)
    slogan = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Site Settings'

    def save(self, *args, **kwargs):
        if not self.id and SiteSettings.objects.exists():
            return None
        return super(SiteSettings,self).save(*args,**kwargs)

    def __str__ (self):
        return "Setting"
    
class Subscribe(models.Model):
    email = models.EmailField(max_length=256)

    def __str__(self):
        return self.email
    
class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=256)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.subject
    
class Site_smedia(models.Model):
    facebook = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    google = models.URLField(max_length=200)
    pinterest = models.URLField(max_length=200)

    def __str__(self):
        return "Site_smedia"
    
class BlogCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class BlogTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Blog(models.Model):
    image = models.ImageField(upload_to="blog_images")
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    short_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(BlogCategory, related_name="categoryblogs")
    tags = models.ManyToManyField(BlogTag, related_name="tagblogs")
    content = HTMLField()
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    email = models.EmailField(max_length=256)
    website = models.CharField(max_length=256, blank=True,null=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="replies", blank=True, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.content  