# Generated by Django 5.0.1 on 2024-03-29 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_supportingimage_post_supportingimage2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='supportingimage',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
        migrations.AlterField(
            model_name='post',
            name='supportingimage2',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
        migrations.AlterField(
            model_name='post',
            name='supportingimage3',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]
