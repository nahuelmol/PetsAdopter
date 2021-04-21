# Generated by Django 3.2 on 2021-04-21 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20210421_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='coin',
            field=models.CharField(default='Dollar', max_length=20),
        ),
        migrations.AlterField(
            model_name='client',
            name='crypto',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='client',
            name='fond',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='client',
            name='valoration',
            field=models.IntegerField(default=2),
        ),
    ]
