# Generated by Django 2.1.5 on 2019-01-16 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0004_auto_20190116_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='views_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]