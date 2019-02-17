from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class UserDetail(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,unique=True)
    website = models.URLField(max_length=200, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    facebook_id = models.CharField(max_length=50, blank=True)
    twitter_id = models.CharField(max_length=50, blank=True)
    linkedin_id = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.website

class UserBlog(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name = "userblog")
    #blog type choices
    WORDPRESS = 'WP'
    TUMBLR = 'TM'
    MEDIUM = 'ME'
    BLOG_CHOICES = (
        (WORDPRESS, 'Wordpress'),
        (TUMBLR, 'Tumblr'),
        (MEDIUM, 'Medium'),
    )
    blog_type = models.CharField(
        max_length=2,
        choices=BLOG_CHOICES,
        default=WORDPRESS,
    )
    blog_url = models.URLField(max_length=200, blank = False)

    def __str__(self):
        return self.blog_url