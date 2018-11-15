# Generated by Django 2.1 on 2018-11-15 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classroom', '0001_initial'),
        ('language', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('day', models.CharField(max_length=15)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('description', models.TextField(max_length=255)),
                ('classroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classroom.Classroom')),
                ('lan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='language.Language')),
            ],
        ),
    ]
