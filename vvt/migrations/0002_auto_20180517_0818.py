# Generated by Django 2.0.5 on 2018-05-17 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vvt', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='processingactivity',
            old_name='transfer',
            new_name='transfer_recipient',
        ),
    ]
