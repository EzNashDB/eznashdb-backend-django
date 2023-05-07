# Generated by Django 4.0.1 on 2023-05-07 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eznashdb', '0006_remove_shul_enum_has_kaddish_alone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='relative_size',
            field=models.CharField(blank=True, choices=[('XS', 'Much smaller'), ('S', 'Smaller'), ('M', 'Same size'), ('L', 'Larger')], max_length=50, null=True),
        ),
    ]