# Generated by Django 3.1.7 on 2021-03-13 18:21

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_student', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='school.user')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField(blank=True, default='')),
                ('father_name', models.CharField(max_length=100, null=True)),
                ('mother_name', models.CharField(max_length=100, null=True)),
                ('avatar_url', models.CharField(max_length=255, null=True)),
                ('level', models.IntegerField(null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('avatar', models.ImageField(upload_to='avatars')),
            ],
        ),
    ]
