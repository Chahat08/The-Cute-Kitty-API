# Generated by Django 4.1.2 on 2022-10-18 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kitty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='536', max_length=100)),
                ('img', models.ImageField(blank=True, upload_to='cats/')),
                ('breed', models.CharField(blank=True, default='cute', max_length=100)),
            ],
        ),
    ]