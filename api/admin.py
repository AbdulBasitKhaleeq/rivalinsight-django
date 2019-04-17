from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserDetail)
admin.site.register(UserBlog)

admin.site.register(FacebookReport)
admin.site.register(TwitterReport)
admin.site.register(WordpressReport)
admin.site.register(TumblrReport)


admin.site.register(FacebookTrending)
admin.site.register(TwitterTrending)
admin.site.register(NewsTrending)
admin.site.register(TumblrTrending)