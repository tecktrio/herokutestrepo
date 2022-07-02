# Generated by Django 3.2.5 on 2022-07-02 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.TextField()),
                ('pro_description', models.TextField()),
                ('pro_rate', models.IntegerField()),
                ('pro_img', models.ImageField(upload_to='')),
            ],
        ),
    ]
