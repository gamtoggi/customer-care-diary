# Generated by Django 2.1.5 on 2019-01-25 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_contactmemo'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmemo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='contactmemo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]