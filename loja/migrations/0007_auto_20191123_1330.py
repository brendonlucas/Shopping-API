# Generated by Django 2.2.6 on 2019-11-23 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0006_auto_20191123_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='cliente',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]