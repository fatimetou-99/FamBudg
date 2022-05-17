# Generated by Django 4.0 on 2022-01-30 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('ressources', '0005_family_rename_max_amout_category_max_amount_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='family',
            options={'verbose_name': 'Family'},
        ),
        migrations.AddField(
            model_name='depency',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.RemoveField(
            model_name='category',
            name='user',
        ),
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
