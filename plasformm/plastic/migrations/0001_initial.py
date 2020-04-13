# Generated by Django 3.0.4 on 2020-03-06 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('company', models.CharField(max_length=100, verbose_name='Компания')),
                ('email', models.EmailField(max_length=254)),
                ('number', models.PositiveIntegerField(default=0, verbose_name='Телефон')),
                ('description', models.TextField(verbose_name='Сообщение')),
            ],
        ),
    ]
