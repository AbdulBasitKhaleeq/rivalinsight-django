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
    username = models.CharField(max_length=50, blank = True)
    password = models.CharField(max_length=16, blank = True)
    def __str__(self):
        return self.blog_url


class FacebookReport(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pageName = models.CharField(max_length = 250)
    likes = models.IntegerField(default = 0)
    followers = models.IntegerField(default = 0)
    maleUsers = models.IntegerField(default = 0)
    femaleUsers = models.IntegerField(default = 0)
    totalPosts = models.IntegerField(default = 0)
    sentimentPosts = models.TextField(blank = True)
    sentimentComments = models.TextField(blank = True)

    def __str__(self):
        return self.pageName





class TwitterReport(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pageName = models.CharField(max_length = 250)
    following = models.IntegerField(default = 0)
    followers = models.IntegerField(default = 0)
    maleUsers = models.IntegerField(default = 0)
    femaleUsers = models.IntegerField(default = 0)
    totalTweets = models.IntegerField(default = 0)
    sentimentTweets = models.TextField(blank = True)
    sentimentReplies = models.TextField(blank = True)
    keywords = models.TextField(max_length = 400, blank = True)
    loaction = models.CharField(max_length = 250, blank = True)


    def __str__(self):
        return self.pageName

class TumblrReport(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pageName = models.CharField(max_length = 250)
    keywords = models.TextField(max_length = 400, blank = True)
    likes = models.IntegerField(default = 0)
    followers = models.IntegerField(default = 0)
    maleUsers = models.IntegerField(default = 0)
    femaleUsers = models.IntegerField(default = 0)
    totalPosts = models.IntegerField(default = 0)
    sentimentPosts = models.TextField(blank = True)
    sentimentComments = models.TextField(blank = True)

    def __str__(self):
        return self.pageName

class WordpressReport(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    blogName = models.CharField(max_length = 250)
    keywords = models.TextField(max_length = 400, blank = True)
    sentimentPosts = models.TextField(blank = True)
    sentimentComments = models.TextField(blank = True)
    totalPosts = models.IntegerField(default = 0)
    totalAuthors = models.IntegerField(default = 0)
    newPosts = models.IntegerField(default = 0)
    newComments = models.IntegerField(default = 0)
    totalComments = models.IntegerField(default = 0)
    avgPostLength = models.IntegerField(default = 0)

    def __str__(self):
        return self.blogName



### trending Content of competitors:
class FacebookTrending(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField(max_length = 500, blank = True)
    topics = models.CharField(max_length = 100,blank = True)
    engagement = models.CharField(max_length = 10,blank = True)
    trendingScore = models.CharField(max_length = 10,blank = True)
    source = models.CharField(max_length = 50,blank = False)
    sentiment = models.IntegerField(default = 0)

    def __str__(self):
        return self.source


class TwitterTrending(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField(max_length = 200, blank = True)
    topics = models.CharField(max_length = 100,blank = True)
    engagement = models.CharField(max_length = 10,blank = True)
    trendingScore = models.CharField(max_length = 10,blank = True)
    source = models.CharField(max_length = 50,blank = False)
    sentiment = models.IntegerField(default = 0)

    def __str__(self):
        return self.source


class TumblrTrending(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField(max_length = 200, blank = True)
    topics = models.CharField(max_length = 100,blank = True)
    engagement = models.CharField(max_length = 10,blank = True)
    trendingScore = models.CharField(max_length = 10,blank = True)
    source = models.CharField(max_length = 50,blank = False)
    sentiment = models.IntegerField(default = 0)

    def __str__(self):
        return self.source


class NewsTrending(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    heading = models.CharField(max_length = 250)
    content = models.TextField(max_length = 800, blank = True)
    topics = models.CharField(max_length = 100,blank = True)
    source = models.CharField(max_length = 50,blank = False)
    imageUrl = models.CharField(max_length = 250, blank = True)
    sentiment = models.IntegerField(default = 0)

    def __str__(self):
        return self.source