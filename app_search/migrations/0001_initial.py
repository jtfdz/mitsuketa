# Generated by Django 4.0.6 on 2022-07-12 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_manga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id_manga', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('clicks', models.PositiveIntegerField()),
                ('author', models.CharField(max_length=100)),
                ('last_update', models.DateField(auto_now=True)),
                ('chapters', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[(0, 'completed'), (1, 'on-going'), (2, 'hiatus'), (3, 'dropped')], max_length=1)),
                ('genres', models.ManyToManyField(to='app_manga.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id_page', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('manga_offered', models.ManyToManyField(to='app_search.manga')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id_page', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('manga_offered', models.ManyToManyField(to='app_search.manga')),
            ],
        ),
    ]