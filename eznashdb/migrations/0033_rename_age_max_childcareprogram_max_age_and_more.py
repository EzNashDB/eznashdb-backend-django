# Generated by Django 4.0.1 on 2024-01-01 18:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("eznashdb", "0032_alter_childcareprogram_age_max_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="childcareprogram",
            old_name="age_max",
            new_name="max_age",
        ),
        migrations.RenameField(
            model_name="childcareprogram",
            old_name="age_min",
            new_name="min_age",
        ),
    ]