# Generated by Django 2.0rc1 on 2017-12-06 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='img'),
        ),
    ]
