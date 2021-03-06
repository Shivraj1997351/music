# Generated by Django 3.2.6 on 2021-09-30 05:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowersCount',
            fields=[
                ('follower_id', models.AutoField(primary_key=True, serialize=False)),
                ('follower', models.CharField(max_length=100)),
                ('singer', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='likesCount',
            fields=[
                ('liker_id', models.AutoField(primary_key=True, serialize=False)),
                ('liker', models.CharField(max_length=100)),
                ('song_id', models.CharField(max_length=200000000)),
            ],
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('sing_id', models.AutoField(primary_key=True, serialize=False)),
                ('singer', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('singer', models.CharField(max_length=200)),
                ('tags', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images')),
                ('song', models.FileField(upload_to='songs')),
                ('movie', models.CharField(default='NA', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Watchlater',
            fields=[
                ('watch_id', models.AutoField(primary_key=True, serialize=False)),
                ('video_id', models.CharField(max_length=200000000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('hist_id', models.AutoField(primary_key=True, serialize=False)),
                ('music_id', models.CharField(max_length=200000000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
