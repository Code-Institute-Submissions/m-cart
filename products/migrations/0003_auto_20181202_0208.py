# Generated by Django 2.0.8 on 2018-12-02 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productsize'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productsize',
            old_name='size_image',
            new_name='image',
        ),
    ]