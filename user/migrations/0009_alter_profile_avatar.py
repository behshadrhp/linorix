# Generated by Django 4.1 on 2022-08-25 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0008_alter_skill_description_alter_skill_label"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(
                default="/static/avatar/6.png", upload_to="profile/"
            ),
        ),
    ]
