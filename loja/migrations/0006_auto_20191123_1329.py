# Generated by Django 2.2.6 on 2019-11-23 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loja', '0005_compra'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('cpf', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=250)),
                ('endereco', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('cliente_complement', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cliente_complement', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='compra',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.Cliente'),
        ),
    ]
