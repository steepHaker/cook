# Generated by Django 4.2.2 on 2023-06-16 23:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='tag',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='tag',
            new_name='slug',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='directions',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingrediends',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
