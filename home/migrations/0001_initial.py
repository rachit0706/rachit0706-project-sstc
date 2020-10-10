# Generated by Django 3.1.1 on 2020-09-09 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
    ]
