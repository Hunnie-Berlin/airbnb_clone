# Generated by Django 2.2.5 on 2020-09-21 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200921_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email_confirmation',
            new_name='email_verified',
        ),
        migrations.AddField(
            model_name='user',
            name='email_secret',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
