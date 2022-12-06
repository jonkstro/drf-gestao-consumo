# Generated by Django 4.1.3 on 2022-12-01 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dispositivo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leitura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leitura', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('dispositivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispositivo.dispositivo')),
            ],
        ),
    ]