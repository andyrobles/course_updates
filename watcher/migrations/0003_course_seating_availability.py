# Generated by Django 2.2.1 on 2020-03-22 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watcher', '0002_auto_20200319_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='seating_availability',
            field=models.CharField(default='poop', max_length=200),
            preserve_default=False,
        ),
    ]