# Generated by Django 3.1.1 on 2020-09-16 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200917_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentproject',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
