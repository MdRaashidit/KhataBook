# Generated by Django 3.1.2 on 2021-01-06 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dbname', models.CharField(max_length=30)),
                ('dbnumber', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('balance', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dbdate', models.DateField()),
                ('dbamount', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('description', models.CharField(max_length=30)),
                ('dbparty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='udhaar.party')),
            ],
        ),
    ]