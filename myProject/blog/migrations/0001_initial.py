# Generated by Django 4.1.3 on 2022-11-19 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('datePost', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
