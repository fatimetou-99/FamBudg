# Generated by Django 4.0 on 2022-01-23 12:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ressources', '0004_remove_depency_votes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.TextField()),
                ('salary', models.DecimalField(decimal_places=10, max_digits=19)),
                ('pourcentage', models.TextField()),
            ],
            options={
                'verbose_name': 'Famille',
            },
        ),
        migrations.RenameField(
            model_name='category',
            old_name='max_amout',
            new_name='max_amount',
        ),
        migrations.RemoveField(
            model_name='category',
            name='user',
        ),
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
