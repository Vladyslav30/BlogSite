# Generated by Django 4.1.7 on 2023-04-01 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=200)),
                ('post_text', models.TextField()),
                ('post_date', models.DateTimeField(verbose_name='date published')),
                ('post_image', models.ImageField(upload_to='post_images/')),
            ],
        ),
    ]
