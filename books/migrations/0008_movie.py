# Generated by Django 4.2.1 on 2023-05-28 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_book_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('author', models.CharField(blank=True, max_length=50)),
                ('year', models.IntegerField()),
                ('raiting', models.IntegerField(default=0)),
            ],
        ),
    ]
