# Generated by Django 5.0.6 on 2024-07-04 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_Management', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(related_name='students', to='Student_Management.subject'),
        ),
    ]
