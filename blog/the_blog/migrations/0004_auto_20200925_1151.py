# Generated by Django 3.1.1 on 2020-09-25 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_blog', '0003_post_creating_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creating_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
