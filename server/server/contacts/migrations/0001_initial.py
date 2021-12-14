# Generated by Django 4.0 on 2021-12-12 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullName', models.CharField(max_length=255, null=True)),
                ('password', models.CharField(max_length=255, null=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('temporalCode', models.UUIDField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.user')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userId', models.BigIntegerField(null=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('messages', models.ManyToManyField(to='contacts.Message')),
            ],
        ),
    ]