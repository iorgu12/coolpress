# Generated by Django 3.2.8 on 2021-10-20 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import press.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='CoolUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github_profile', models.CharField(blank=True, max_length=150, null=True)),
                ('gh_repositories', models.IntegerField(blank=True, null=True)),
                ('gravatar_link', models.CharField(blank=True, max_length=400, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('body', models.TextField()),
                ('image_link', models.CharField(blank=True, max_length=400, null=True)),
                ('word_cloud_link', models.CharField(blank=True, max_length=400, null=True)),
                ('source_link', models.CharField(blank=True, max_length=400, null=True)),
                ('source_label', models.CharField(blank=True, max_length=400, null=True)),
                ('status', models.CharField(choices=[('DRAFT', 'Draft'), ('PUBLISHED', 'Published post')], default=press.models.PostStatus['DRAFT'], max_length=32)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='press.cooluser')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='press.category')),
            ],
        ),
    ]
