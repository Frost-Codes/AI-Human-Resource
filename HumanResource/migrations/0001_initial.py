# Generated by Django 4.2.13 on 2024-06-05 10:56

import HumanResource.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Prefer not to say', 'Prefer not to say')], max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(choices=[('Nairobi, Kenya', 'Nairobi, Kenya'), ('California, US', 'California, US'), ('London, UK', 'London UK'), ('San fransisco, US', 'San fransisco, US'), ('Cape Town, SA', 'Cape Town, SA')], max_length=100)),
                ('cv', models.FileField(upload_to='cvs/', validators=[HumanResource.models.validate_pdf])),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('department', models.CharField(choices=[('HR', 'Human Resource'), ('IT', 'Information Technology'), ('Marketing', 'Marketing'), ('Finance', 'Finance'), ('R&D', 'Research and Development')], max_length=50)),
                ('salary', models.IntegerField()),
                ('location', models.CharField(choices=[('Nairobi, Kenya', 'Nairobi, Kenya'), ('California, US', 'California, US'), ('London, UK', 'London UK'), ('San fransisco, US', 'San fransisco, US'), ('Cape Town, SA', 'Cape Town, SA')], max_length=100)),
                ('introduction', models.CharField(max_length=220)),
                ('brief_posting_description', models.CharField(max_length=400)),
                ('responsibilities', models.CharField(max_length=2000)),
                ('qualifications', models.CharField(max_length=1500)),
                ('is_active', models.BooleanField(default=True)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('shortlist', models.ManyToManyField(blank=True, related_name='shortlisted_jobs', to='HumanResource.applicant')),
            ],
        ),
        migrations.AddField(
            model_name='applicant',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicants', to='HumanResource.job'),
        ),
    ]
