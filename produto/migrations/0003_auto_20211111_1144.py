# Generated by Django 3.2.9 on 2021-11-11 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_auto_20211111_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='codigo_02',
            field=models.CharField(default='-', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='codigo_03',
            field=models.CharField(default='-', max_length=10, null=True),
        ),
    ]