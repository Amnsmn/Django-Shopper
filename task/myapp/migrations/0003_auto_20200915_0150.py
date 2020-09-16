# Generated by Django 3.1.1 on 2020-09-14 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200914_2203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='quantity',
            new_name='count',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='product',
            new_name='product_fk',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='user_fk',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='stock',
            new_name='available',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='productTitle',
            new_name='product_name',
        ),
    ]