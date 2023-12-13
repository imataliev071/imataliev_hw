# Generated by Django 5.0 on 2023-12-13 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('book_image', models.ImageField(upload_to='')),
                ('book_description', models.TextField()),
                ('book_creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]