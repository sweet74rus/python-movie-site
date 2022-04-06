# Generated by Django 4.0.3 on 2022-04-06 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Жанр')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Жанры',
                'verbose_name_plural': 'Жанры',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название фильма')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('movie_image', models.ImageField(upload_to='', verbose_name='Обложка фильма')),
                ('rating', models.FloatField(verbose_name='Рейтинг фильма')),
                ('description', models.TextField(verbose_name='Описание фильма')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name_plural': 'Фильмы',
            },
        ),
    ]
