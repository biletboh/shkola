# Generated by Django 2.0.6 on 2018-07-18 07:53

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180718_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_pl',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='photos/blog', verbose_name='Світлина польською'),
        ),
    ]