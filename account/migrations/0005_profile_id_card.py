# Generated by Django 3.2 on 2021-06-21 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20210620_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='id_card',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
