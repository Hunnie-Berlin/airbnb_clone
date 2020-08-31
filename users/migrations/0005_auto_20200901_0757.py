# Generated by Django 2.2.5 on 2020-08-31 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200901_0753'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='superhost',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='currency',
            field=models.CharField(blank=True, choices=[('USD', 'USD'), ('KRW', 'KRW'), ('EUR', 'EUR')], max_length=3, null=True),
        ),
    ]
