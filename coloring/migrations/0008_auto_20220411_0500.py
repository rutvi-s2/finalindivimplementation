# Generated by Django 3.1.5 on 2022-04-11 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coloring', '0007_auto_20220411_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coord',
            name='x',
            field=models.DecimalField(decimal_places=4, max_digits=8),
        ),
        migrations.AlterField(
            model_name='coord',
            name='y',
            field=models.DecimalField(decimal_places=4, max_digits=8),
        ),
    ]