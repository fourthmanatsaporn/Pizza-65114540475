# Generated by Django 5.0.6 on 2024-12-18 15:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Pizza", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=150, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]