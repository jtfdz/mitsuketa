# Generated by Django 4.0.6 on 2022-07-13 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_search', '0006_rename_id_tags_tags_id_tag_remove_manga_tags_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='volumes',
            field=models.PositiveIntegerField(default=3),
            preserve_default=False,
        ),
    ]
