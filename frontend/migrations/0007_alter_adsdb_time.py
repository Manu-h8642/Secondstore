# Generated by Django 5.0.2 on 2024-04-02 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_wishlistdb_alter_userprofile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adsdb',
            name='time',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]