# Generated by Django 5.0.2 on 2024-02-15 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_alter_adsdb_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='adsdb',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
