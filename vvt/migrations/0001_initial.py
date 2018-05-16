# Generated by Django 2.0.5 on 2018-05-15 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Categories of personal data')),
            ],
        ),
        migrations.CreateModel(
            name='PersonCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Category of affected individuals')),
            ],
        ),
        migrations.CreateModel(
            name='RecipientCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Categories of recipients')),
            ],
        ),
        migrations.CreateModel(
            name='Verarbeitung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Processing Activity')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created on')),
                ('changed', models.DateField(auto_now=True, verbose_name='Changed on')),
                ('responsible', models.TextField(verbose_name='Responsible')),
                ('reason', models.TextField(verbose_name='Reason')),
                ('transfer', models.TextField(verbose_name='Transfer to third countries')),
                ('transfer_warrant', models.TextField(verbose_name='Transfer warrant')),
                ('retention', models.CharField(max_length=200, verbose_name='Retention period')),
                ('processors', models.TextField(verbose_name='Order processors')),
                ('data_categories', models.ManyToManyField(to='vvt.DataCategory', verbose_name='Categories of personal data')),
                ('person_categories', models.ManyToManyField(to='vvt.PersonCategory', verbose_name='Categories of affected individuals')),
                ('recipient_categories', models.ManyToManyField(to='vvt.RecipientCategory', verbose_name='Categories of recipients')),
            ],
        ),
    ]