# Generated by Django 3.2.9 on 2021-11-11 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_produto_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='image',
            field=models.ImageField(upload_to='produto/images/'),
        ),
    ]