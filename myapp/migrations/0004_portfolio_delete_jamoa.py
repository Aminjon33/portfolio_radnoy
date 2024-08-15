# Generated by Django 5.1 on 2024-08-15 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_about_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='portfolio/')),
                ('client', models.CharField(max_length=100)),
                ('website', models.URLField()),
                ('completed_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Jamoa',
        ),
    ]
