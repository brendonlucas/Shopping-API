# Generated by Django 2.2.6 on 2019-11-20 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='loja',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='Loja_pertencente', to='loja.Loja'),
            preserve_default=False,
        ),
    ]
