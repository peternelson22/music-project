# Generated by Django 4.1.6 on 2023-02-16 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='blankimage.png', upload_to='images/users'),
        ),
    ]