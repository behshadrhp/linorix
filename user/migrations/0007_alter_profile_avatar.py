# Generated by Django 4.1 on 2022-08-25 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0006_alter_profile_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(
                default="/static/avatar/3.png", upload_to="profile/"
            ),
        ),
    ]
