# Generated by Django 2.1.1 on 2018-09-10 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lw2', '0008_auto_20180910_0440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='base_score',
            field=models.IntegerField(default=1),
        ),
    ]
