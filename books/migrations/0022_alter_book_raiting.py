# Generated by Django 4.2.1 on 2023-06-09 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0021_alter_book_raiting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='raiting',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
