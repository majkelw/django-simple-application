# Generated by Django 3.1.7 on 2021-03-24 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('color', models.CharField(max_length=40)),
                ('gender', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Hunting',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('duration', models.IntegerField(default=0)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cat')),
            ],
        ),
        migrations.CreateModel(
            name='Prey',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='UserCatOwner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='HuntingDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cat')),
                ('hunting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hunting')),
                ('prey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.prey')),
            ],
        ),
    ]
