# Generated by Django 2.1.1 on 2018-09-10 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lw2', '0006_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='vote_count',
            field=models.IntegerField(default=0),
        ),
    ]
