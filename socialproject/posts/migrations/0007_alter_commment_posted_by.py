# Generated by Django 5.0.3 on 2024-04-04 22:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0006_commment_posted_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commment",
            name="posted_by",
            field=models.CharField(max_length=100),
        ),
    ]