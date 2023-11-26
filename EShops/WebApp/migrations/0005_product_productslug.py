# Generated by Django 4.2.5 on 2023-11-21 16:43

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0004_product_category_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productslug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True),
        ),
    ]
