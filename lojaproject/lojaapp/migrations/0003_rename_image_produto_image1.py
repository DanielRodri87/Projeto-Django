# Generated by Django 4.1.5 on 2023-01-29 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lojaapp', '0002_produto_image2_produto_image3_produto_image4'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='image',
            new_name='image1',
        ),
    ]
