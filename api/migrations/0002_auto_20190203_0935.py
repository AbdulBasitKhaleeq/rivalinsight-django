# Generated by Django 2.1.5 on 2019-02-03 04:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserBlogs',
            new_name='UserBlog',
        ),
        migrations.RenameModel(
            old_name='UserDetails',
            new_name='UserDetail',
        ),
    ]