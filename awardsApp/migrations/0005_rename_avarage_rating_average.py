# Generated by Django 4.0.5 on 2022-06-11 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awardsApp', '0004_rename_avarage_rate_rating_avarage_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='avarage',
            new_name='average',
        ),
    ]