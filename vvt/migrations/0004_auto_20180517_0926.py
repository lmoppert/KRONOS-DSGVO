# Generated by Django 2.0.5 on 2018-05-17 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vvt', '0003_auto_20180517_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processingactivity',
            name='processors',
            field=models.TextField(blank=True, verbose_name='Order processors'),
        ),
        migrations.AlterField(
            model_name='processingactivity',
            name='transfer_warrant',
            field=models.TextField(blank=True, verbose_name='Transfer warrant'),
        ),
    ]