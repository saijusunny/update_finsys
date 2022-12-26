# Generated by Django 4.0.4 on 2022-11-08 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0032_alter_purchase_expense_file_alter_purchaseorder_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=150),
        ),
        migrations.AlterField(
            model_name='accounts1',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
