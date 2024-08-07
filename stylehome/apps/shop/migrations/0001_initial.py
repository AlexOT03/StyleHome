# <<<<<<< HEAD
# # Generated by Django 5.0.6 on 2024-08-07 03:29
# =======
# # Generated by Django 5.0.6 on 2024-08-07 03:07
# >>>>>>> b1cada59d1cf5d583ad86d61ec0b6423fcdf084e

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acabado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='categories/')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('price', models.FloatField(default=0.0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('measurements', models.CharField(max_length=150)),
                ('acabado_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.acabado')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
                ('color_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.color')),
                ('material_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.material')),
            ],
        ),
    ]
