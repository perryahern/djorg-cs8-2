# Generated by Django 2.0.6 on 2018-06-26 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0002_auto_20180626_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='note',
            field=models.TextField(blank=True),
        ),
    ]
