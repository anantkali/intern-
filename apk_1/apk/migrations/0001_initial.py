# Generated by Django 2.2.18 on 2021-09-06 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('pass_1', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('pass_1', models.CharField(max_length=256)),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('Country', models.CharField(max_length=20)),
                ('Zip_code', models.IntegerField()),
            ],
        ),
    ]
