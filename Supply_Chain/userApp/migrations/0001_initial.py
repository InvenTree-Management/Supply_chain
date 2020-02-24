# Generated by Django 2.0.4 on 2020-02-23 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='HospitalItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='HospitalOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested', models.DateTimeField(max_length=100, null=True)),
                ('received', models.DateTimeField(max_length=100, null=True)),
                ('quantity_requested', models.IntegerField(default=0)),
                ('HospitalStatus', models.TextField(max_length=100)),
                ('SupplierStatus', models.CharField(choices=[('REC', 'Received'), ('REQ', 'Requested')], default='REQ', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='HospitalProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('hospital_code', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('item_code', models.CharField(max_length=50)),
                ('manufacture_date', models.DateTimeField()),
                ('expiry_date', models.TimeField()),
                ('items_available', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SupplierCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.ItemCategory')),
            ],
        ),
        migrations.CreateModel(
            name='SupplierItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.Item')),
                ('item_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.SupplierCategory')),
            ],
        ),
        migrations.CreateModel(
            name='SupplierOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received', models.DateTimeField(max_length=100, null=True)),
                ('dispatched', models.DateTimeField(max_length=100, null=True)),
                ('quantity_dispatched', models.IntegerField(default=0)),
                ('hospital_code', models.CharField(max_length=100)),
                ('SupplierStatus', models.CharField(choices=[('REC', 'Received'), ('DIS', 'Dispatched'), ('PEN', 'Pending'), ('DEL', 'Delivered')], default='REC', max_length=3)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.Item')),
            ],
        ),
        migrations.CreateModel(
            name='SupplierProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.HospitalProfile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='suppliercategory',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.SupplierProfile'),
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.ItemCategory'),
        ),
        migrations.AddField(
            model_name='hospitalorder',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.Item'),
        ),
        migrations.AddField(
            model_name='hospitalitems',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.Item'),
        ),
        migrations.AddField(
            model_name='hospitalitems',
            name='item_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.HospitalCategory'),
        ),
        migrations.AddField(
            model_name='hospitalcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.ItemCategory'),
        ),
        migrations.AddField(
            model_name='hospitalcategory',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.HospitalProfile'),
        ),
    ]
