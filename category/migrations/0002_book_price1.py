# Generated by Django 4.2.4 on 2023-09-04 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price1',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
