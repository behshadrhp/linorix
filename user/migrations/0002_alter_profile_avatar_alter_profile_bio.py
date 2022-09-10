# Generated by Django 4.1.1 on 2022-09-10 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(
                default="/static/avatar/7.png", upload_to="profile/"
            ),
        ),
        migrations.AlterField(
            model_name="profile", name="bio", field=models.TextField(max_length=255),
        ),
    ]
