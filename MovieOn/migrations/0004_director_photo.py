# Generated by Django 3.1.1 on 2020-12-09 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieOn', '0003_auto_20201021_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='photo',
            field=models.URLField(null=True),
        ),
    ]