# Generated by Django 3.1.6 on 2021-02-07 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
