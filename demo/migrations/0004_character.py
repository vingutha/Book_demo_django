# Generated by Django 4.2.7 on 2023-11-19 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_booknumber_book_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.book')),
            ],
        ),
    ]
