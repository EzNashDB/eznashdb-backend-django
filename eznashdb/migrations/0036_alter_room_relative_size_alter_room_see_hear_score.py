# Generated by Django 4.0.1 on 2024-03-27 19:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("eznashdb", "0035_remove_shul_has_childcare_shul_has_no_childcare"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="relative_size",
            field=models.CharField(
                blank=True,
                choices=[
                    ("S", "S: Less than half of men's"),
                    ("M", "M: Smaller than men's, but at least half"),
                    ("L", "L: Same size as men's or larger"),
                ],
                default="",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="see_hear_score",
            field=models.CharField(
                blank=True,
                choices=[
                    ("5", "5: Equal to men's"),
                    ("4", "4"),
                    ("3", "3"),
                    ("2", "2"),
                    ("1", "1: Much more difficult"),
                ],
                default="",
                max_length=50,
            ),
        ),
    ]
