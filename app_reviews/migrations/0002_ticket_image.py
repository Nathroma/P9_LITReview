# Generated by Django 3.2.2 on 2021-05-31 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='image',
            field=models.ImageField(default='images/upload/NULL.jpg', upload_to='images/upload/'),
        ),
    ]
