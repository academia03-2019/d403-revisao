# Generated by Django 2.2.1 on 2019-05-06 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poxa_crush', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crush',
            name='foto',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
