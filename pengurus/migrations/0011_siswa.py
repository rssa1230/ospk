# Generated by Django 3.2.16 on 2023-01-22 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pengurus', '0010_auto_20230122_0436'),
    ]

    operations = [
        migrations.CreateModel(
            name='Siswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nis', models.CharField(max_length=10)),
                ('nama', models.CharField(max_length=50)),
                ('kelas_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pengurus.kelas')),
            ],
        ),
    ]