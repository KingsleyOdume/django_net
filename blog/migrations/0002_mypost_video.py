# Generated by Django 2.2.9 on 2019-12-22 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mypost',
            name='video',
            field=models.ImageField(null=True, upload_to='video\\'),
        ),
    ]
