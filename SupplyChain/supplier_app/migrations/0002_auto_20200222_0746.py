# Generated by Django 2.0.4 on 2020-02-22 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='expiry_date',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='items_available',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='manufacture_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='itemcategory',
            name='item_category',
            field=models.CharField(max_length=100),
        ),
    ]
