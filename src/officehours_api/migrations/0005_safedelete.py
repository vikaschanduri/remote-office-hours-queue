# Generated by Django 3.0.4 on 2020-03-20 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officehours_api', '0004_remove_host_for_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='queue',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]