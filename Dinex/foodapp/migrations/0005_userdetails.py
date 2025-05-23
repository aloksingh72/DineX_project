# Generated by Django 4.2.14 on 2025-03-31 12:45

from django.db import migrations, models
import foodapp.manager


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0004_product_sub_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('confirm_password', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'user_details',
            },
            managers=[
                ('objects', foodapp.manager.CustomUserManager()),
            ],
        ),
    ]
