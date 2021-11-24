# Generated by Django 3.2.9 on 2021-11-08 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='hashtag',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='uploader',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='photo',
            name='upload_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]