# Generated by Django 4.0.4 on 2022-12-02 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0034_expense2_remove_purchase_expense_destinofsupply_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profit_loss',
            name='payments',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
