# Generated by Django 4.2.1 on 2023-07-07 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0029_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='count',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
    ]
