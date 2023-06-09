# Generated by Django 4.2 on 2023-04-25 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voyage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_buses', models.IntegerField(max_length=10)),
                ('cost_transportation', models.IntegerField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_restaurant_lunch', models.CharField(max_length=30)),
                ('completed_lunch', models.BooleanField()),
                ('cost_lunch', models.IntegerField(max_length=1000, null=True)),
                ('satisfaction_lunch', models.IntegerField(max_length=5, null=True)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voyage.day')),
            ],
        ),
        migrations.CreateModel(
            name='Dinner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_restaurant_dinner', models.CharField(max_length=30)),
                ('cost_dinner', models.IntegerField(max_length=1000, null=True)),
                ('completed_dinner', models.BooleanField()),
                ('satisfaction_dinner', models.IntegerField(max_length=5, null=True)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voyage.day')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_activity', models.CharField(max_length=30)),
                ('completed_activity', models.BooleanField()),
                ('cost_activity', models.IntegerField(max_length=1000, null=True)),
                ('satisfaction_activity', models.IntegerField(max_length=5, null=True)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voyage.day')),
            ],
        ),
    ]
