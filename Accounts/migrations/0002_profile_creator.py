# Generated by Django 3.0.6 on 2020-05-13 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='creator',
            field=models.BooleanField(default=False),
        ),
    ]