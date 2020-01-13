# Generated by Django 2.2.8 on 2020-01-13 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eugene', '0003_auto_20200113_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currency',
            name='country',
        ),
        migrations.AddField(
            model_name='currency',
            name='decimal_digits',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='currency',
            name='name_plural',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='currency',
            name='rounding',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='currency',
            name='symbol',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AddField(
            model_name='currency',
            name='symbol_native',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='currency',
            name='code',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
