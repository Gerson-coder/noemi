# Generated by Django 5.1.4 on 2024-12-19 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_is_new_alter_product_is_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Product/product_detail/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Images', to='product.product')),
            ],
        ),
    ]