# Generated by Django 3.1.6 on 2021-02-08 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dxcodes', '0003_auto_20210207_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dxcode',
            name='abbreviated_descrition',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='dxcode',
            name='category_title',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='dxcode',
            name='full_description',
            field=models.TextField(max_length=200),
        ),
    ]