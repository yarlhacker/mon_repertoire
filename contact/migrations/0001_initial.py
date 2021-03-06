# Generated by Django 3.2.4 on 2021-06-11 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ListContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('satuts', models.BooleanField(default=True)),
                ('nom', models.CharField(max_length=250)),
                ('prenom', models.CharField(max_length=250)),
                ('contact', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.FileField(upload_to='images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
