# Generated by Django 3.2.3 on 2021-05-30 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0007_alter_books_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='photo',
            field=models.FileField(blank=True, upload_to='products/%Y/%m/%d/'),
        ),
    ]
