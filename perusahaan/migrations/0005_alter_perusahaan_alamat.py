# Generated by Django 4.1.5 on 2023-01-26 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perusahaan', '0004_alter_perusahaan_alamat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perusahaan',
            name='Alamat',
            field=models.TextField(blank=True, null=True),
        ),
    ]
