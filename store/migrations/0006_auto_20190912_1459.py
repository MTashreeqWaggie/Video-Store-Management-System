# Generated by Django 2.2.5 on 2019-09-12 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20190902_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
