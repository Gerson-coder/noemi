# Generated by Django 5.1.4 on 2024-12-16 20:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Color')),
                ('hex_value', models.CharField(blank=True, max_length=7, null=True, verbose_name='Código HEX')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='Nombre')),
                ('logo', models.ImageField(upload_to='logo_marca/')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': ' Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5, unique=True, verbose_name='Talla')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Description')),
                ('sku', models.CharField(max_length=20, verbose_name='SKU')),
                ('material', models.CharField(blank=True, max_length=50, null=True, verbose_name='Material')),
                ('collection', models.CharField(blank=True, max_length=30, null=True, verbose_name='Colección')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
                ('season', models.CharField(blank=True, choices=[('Spring', 'Primavera'), ('Summer', 'Verano'), ('Fall', 'Otoño'), ('Winter', 'Invierno')], max_length=15, null=True, verbose_name='Temporada')),
                ('gender', models.CharField(blank=True, choices=[('Boy', 'Niño'), ('Girl', 'Niña'), ('Women', 'Mujer'), ('Unisex', 'Unisex')], max_length=10, null=True, verbose_name='Género')),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio con descuento')),
                ('sold_count', models.IntegerField(blank=True, null=True, verbose_name='Cantidad vendida')),
                ('is_featured', models.BooleanField(default=False, verbose_name='Es destacado')),
                ('image', models.ImageField(upload_to='Product')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Está activo')),
                ('average_rating', models.FloatField(default=0.0, verbose_name='Calificación promedio')),
                ('review_count', models.PositiveIntegerField(default=0, verbose_name='Cantidad de reseñas')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('discount_start_date', models.DateField(blank=True, null=True, verbose_name='Inicio del descuento')),
                ('discount_end_date', models.DateField(blank=True, null=True, verbose_name='Fin del descuento')),
                ('categories', models.ManyToManyField(related_name='products', to='product.category')),
                ('marca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.marca')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='Cantidad disponible')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='product.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.size')),
            ],
            options={
                'unique_together': {('product', 'color', 'size')},
            },
        ),
    ]