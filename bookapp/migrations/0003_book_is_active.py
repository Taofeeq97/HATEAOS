# Generated by Django 4.2.2 on 2023-06-20 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0002_rename_desciption_book_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
