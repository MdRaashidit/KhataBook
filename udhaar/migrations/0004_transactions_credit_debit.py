# Generated by Django 3.1.2 on 2021-02-07 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udhaar', '0003_transactions_trace'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='credit_debit',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]