# Generated by Django 2.2.5 on 2019-09-15 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20190912_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedproduct',
            name='returnBy',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookedproduct',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
