# Generated by Django 4.0.1 on 2022-01-14 22:34

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
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DaysVisits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('room', models.IntegerField()),
                ('size', models.FloatField()),
                ('street', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('S', 'Sale'), ('R', 'Rent')], max_length=1)),
                ('type_property', models.CharField(choices=[('A', 'Apartment'), ('H', 'House')], max_length=1)),
                ('number', models.IntegerField()),
                ('description', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='content.city')),
                ('days_visits', models.ManyToManyField(to='content.DaysVisits')),
                ('image', models.ManyToManyField(to='content.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Visits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20)),
                ('schedule', models.TimeField()),
                ('status', models.CharField(choices=[('S', 'Scheduled'), ('F', 'Finished'), ('C', 'Canceled')], default='A', max_length=1)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='content.property')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='schedule',
            field=models.ManyToManyField(to='content.Schedule'),
        ),
    ]