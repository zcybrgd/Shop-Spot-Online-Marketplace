# Generated by Django 4.2.5 on 2023-10-13 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('-created_at',)},
        ),
    ]