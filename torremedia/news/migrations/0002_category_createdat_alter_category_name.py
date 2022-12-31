# Generated by Django 4.1.4 on 2022-12-30 23:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="createdAt",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]
