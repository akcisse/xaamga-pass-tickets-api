# Generated by Django 5.0.6 on 2025-02-04 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_alter_otp_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
