# Generated by Django 4.0 on 2021-12-29 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ressources', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='depency',
            old_name='gategory',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='depency',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='salary',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]