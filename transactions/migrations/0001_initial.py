# Generated by Django 3.2 on 2021-04-20 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('fond', models.FloatField()),
                ('register', models.IntegerField()),
                ('crypto', models.BooleanField()),
                ('coin', models.CharField(max_length=20)),
                ('valoration', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('dest_id', models.IntegerField()),
                ('sender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.client')),
            ],
        ),
    ]
