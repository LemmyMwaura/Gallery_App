# Generated by Django 4.0.3 on 2022-03-29 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_image_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-updated', '-created']},
        ),
    ]