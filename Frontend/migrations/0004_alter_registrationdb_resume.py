# Generated by Django 4.2.2 on 2023-07-03 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0003_registrationdb_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationdb',
            name='Resume',
            field=models.FileField(blank=True, null=True, upload_to='Resume'),
        ),
    ]