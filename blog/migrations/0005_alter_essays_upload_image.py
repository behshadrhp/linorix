# Generated by Django 4.1 on 2022-08-13 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_alter_essays_upload_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="essays",
            name="upload_image",
            field=models.ImageField(default="surface.jpg", upload_to="upload/"),
        ),
    ]
