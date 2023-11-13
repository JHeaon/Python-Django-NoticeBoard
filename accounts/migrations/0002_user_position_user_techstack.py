# Generated by Django 4.2.4 on 2023-11-13 15:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_post_techstack"),
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="position",
            field=models.ManyToManyField(blank=True, to="api.position"),
        ),
        migrations.AddField(
            model_name="user",
            name="techstack",
            field=models.ManyToManyField(blank=True, to="api.techstack"),
        ),
    ]
