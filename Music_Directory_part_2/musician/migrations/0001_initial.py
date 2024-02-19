# Generated by Django 5.0.2 on 2024-02-15 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone_no', models.CharField(max_length=13)),
                ('instrument_type', models.CharField(choices=[('P', 'Percussion'), ('G', 'Guitar'), ('W', 'Woodwind'), ('K', 'Keyboard')], max_length=50)),
            ],
        ),
    ]
