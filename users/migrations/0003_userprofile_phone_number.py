# Generated by Django 4.0.4 on 2022-05-03 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_userprofile_pub_key_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
