# Generated by Django 2.2.3 on 2019-07-25 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_barang', models.CharField(max_length=255)),
                ('deskripsi', models.TextField(max_length=1000)),
                ('pic', models.CharField(max_length=255)),
                ('tanggal_input', models.DateField(auto_now=True)),
            ],
        ),
    ]
