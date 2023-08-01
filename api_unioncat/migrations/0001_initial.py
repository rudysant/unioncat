# Generated by Django 4.2.3 on 2023-08-01 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('author', models.CharField(default='', max_length=200)),
                ('publisher', models.CharField(default='', max_length=200)),
                ('publish_year', models.IntegerField()),
            ],
        ),
    ]