# Generated by Django 4.2.2 on 2023-07-05 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0005_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_or_video_content',
            field=models.FileField(upload_to='post_content'),
        ),
    ]