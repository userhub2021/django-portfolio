# Generated by Django 4.0.6 on 2022-07-29 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_techical_technical'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='コンセプト名')),
                ('explanation', models.TextField(verbose_name='説明')),
                ('github', models.CharField(blank=True, max_length=100, null=True, verbose_name='github')),
            ],
        ),
    ]
