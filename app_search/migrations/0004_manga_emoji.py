# Generated by Django 4.0.6 on 2022-07-12 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_search', '0003_alter_manga_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='emoji',
            field=models.CharField(default='o_o', max_length=10),
            preserve_default=False,
        ),
    ]