# Generated by Django 4.2.4 on 2023-08-28 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ochilgan vaqti')),
                ('update_at', models.DateField(auto_now=True, verbose_name='Ozgargan vaqti')),
                ('full_name', models.CharField(max_length=40, verbose_name='Author ni ismi ')),
                ('bio', models.TextField()),
            ],
            options={
                'verbose_name': 'Muallif',
                'verbose_name_plural': 'Mualliflar',
            },
        ),
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=30, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ochilgan vaqti')),
                ('update_at', models.DateField(auto_now=True, verbose_name='Ozgargan vaqti')),
                ('name', models.CharField(max_length=400)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DiscountImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cher/')),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ochilgan vaqti')),
                ('update_at', models.DateField(auto_now=True, verbose_name='Ozgargan vaqti')),
                ('discount', models.CharField(max_length=300, verbose_name='Chegirma narxi')),
                ('price', models.IntegerField()),
                ('title', models.TextField()),
                ('images', models.ManyToManyField(related_name='images', to='category.discountimage')),
            ],
            options={
                'verbose_name': 'Chegirma',
                'verbose_name_plural': 'Chegirmalar',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ochilgan vaqti')),
                ('update_at', models.DateField(auto_now=True, verbose_name='Ozgargan vaqti')),
                ('name', models.CharField(max_length=50, verbose_name='Kitobni nomi')),
                ('image', models.ImageField(upload_to='book/')),
                ('title', models.TextField()),
                ('price', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
            options={
                'verbose_name': 'Kitob',
                'verbose_name_plural': 'Kitoblar',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ochilgan vaqti')),
                ('update_at', models.DateField(auto_now=True, verbose_name='Ozgargan vaqti')),
                ('name', models.CharField(max_length=50, verbose_name='Blog nomi')),
                ('title', models.TextField()),
                ('img', models.ManyToManyField(related_name='images', to='category.blogimage')),
            ],
            options={
                'verbose_name': 'Yangilik',
                'verbose_name_plural': 'Yangiliklar',
            },
        ),
    ]
