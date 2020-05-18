# Generated by Django 3.0.2 on 2020-05-18 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('name', models.CharField(max_length=250, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, verbose_name='Descripción')),
                ('image', models.ImageField(blank=True, upload_to='images/products')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('code', models.CharField(max_length=30, unique=True, verbose_name='Código')),
                ('value', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.CharField(blank=True, max_length=250, verbose_name='Descripción')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, verbose_name='Descripción')),
                ('image', models.ImageField(blank=True, upload_to='images/providers')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProviderAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('name', models.CharField(max_length=250, verbose_name='Nombre y apellido')),
                ('zip_code', models.CharField(max_length=10, verbose_name='Código postal')),
                ('state', models.CharField(max_length=50, verbose_name='Estado')),
                ('city', models.CharField(max_length=255, verbose_name='Delegación / Municipio')),
                ('colony', models.CharField(max_length=255, verbose_name='Barrio / Colonia / Asentamiento')),
                ('street_name', models.CharField(max_length=255, verbose_name='Calle')),
                ('street_number', models.CharField(max_length=10, verbose_name='N° Exterior')),
                ('internal_number', models.CharField(blank=True, max_length=10, verbose_name='N° Interior / Depto (opcional)')),
                ('between_street1', models.CharField(blank=True, max_length=255, verbose_name='Calle 1')),
                ('between_street2', models.CharField(blank=True, max_length=255, verbose_name='Calle 2')),
                ('telephone', models.CharField(max_length=20, verbose_name='Teléfono de contacto')),
                ('references', models.TextField(max_length=500, verbose_name='Ayuda al repartido a encontrar tu domicilio o el producto que necesitas')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Provider')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('description', models.CharField(max_length=150, verbose_name='Característica del producto')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Precio')),
                ('hierarchy', models.IntegerField(default=1, verbose_name='Jerarquía')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
            options={
                'ordering': ['hierarchy'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Provider'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, to='products.ProductTag'),
        ),
    ]
