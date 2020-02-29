# Generated by Django 2.0.4 on 2020-02-29 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0002_auto_20200226_1600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemcategory',
            options={'verbose_name_plural': 'ItemCategories'},
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='hosp_status',
            field=models.CharField(choices=[('REC', 'Received'), ('DIS', 'Dispatched'), ('PEN', 'Pending'), ('DEL', 'Delivered'), ('REQ', 'Requested')], default='NA', max_length=5),
        ),
        migrations.AddField(
            model_name='order',
            name='hospital_code',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='supp_status',
            field=models.CharField(choices=[('REC', 'Received'), ('DIS', 'Dispatched'), ('PEN', 'Pending'), ('DEL', 'Delivered'), ('REQ', 'Requested')], default='NA', max_length=5),
        ),
    ]
