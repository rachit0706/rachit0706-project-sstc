# Generated by Django 3.1.1 on 2020-09-16 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200914_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentproject',
            name='student_id',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]
