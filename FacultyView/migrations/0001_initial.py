# Generated by Django 5.0.4 on 2024-04-11 12:15

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('s_roll', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('s_fname', models.CharField(default='Nil', max_length=20)),
                ('s_lname', models.CharField(default='Nil', max_length=20)),
                ('s_branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FacultyView.branch')),
                ('s_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FacultyView.section')),
                ('s_year', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='FacultyView.year')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FacultyView.student')),
            ],
        ),
    ]