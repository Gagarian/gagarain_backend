# Generated by Django 3.2.10 on 2021-12-30 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/profile/%Y/%m/%d'),
        ),
    ]
