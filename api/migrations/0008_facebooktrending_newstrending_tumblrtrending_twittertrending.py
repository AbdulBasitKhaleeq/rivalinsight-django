# Generated by Django 2.1.5 on 2019-04-16 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0007_auto_20190329_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookTrending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, max_length=500)),
                ('topics', models.CharField(blank=True, max_length=100)),
                ('engagement', models.CharField(blank=True, max_length=10)),
                ('trendingScore', models.CharField(blank=True, max_length=10)),
                ('source', models.CharField(max_length=50)),
                ('sentiment', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NewsTrending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True, max_length=800)),
                ('topics', models.CharField(blank=True, max_length=100)),
                ('source', models.CharField(max_length=50)),
                ('imageUrl', models.CharField(blank=True, max_length=250)),
                ('sentiment', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TumblrTrending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, max_length=200)),
                ('topics', models.CharField(blank=True, max_length=100)),
                ('engagement', models.CharField(blank=True, max_length=10)),
                ('trendingScore', models.CharField(blank=True, max_length=10)),
                ('source', models.CharField(max_length=50)),
                ('sentiment', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TwitterTrending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, max_length=200)),
                ('topics', models.CharField(blank=True, max_length=100)),
                ('engagement', models.CharField(blank=True, max_length=10)),
                ('trendingScore', models.CharField(blank=True, max_length=10)),
                ('source', models.CharField(max_length=50)),
                ('sentiment', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
