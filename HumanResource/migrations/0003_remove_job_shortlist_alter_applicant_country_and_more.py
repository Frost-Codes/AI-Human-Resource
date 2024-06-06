# Generated by Django 4.2.13 on 2024-06-06 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HumanResource', '0002_alter_job_responsibilities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='shortlist',
        ),
        migrations.AlterField(
            model_name='applicant',
            name='country',
            field=models.CharField(choices=[('Nairobi, Kenya', 'Nairobi, Kenya'), ('California, US', 'California, US'), ('London, UK', 'London, UK'), ('San fransisco, US', 'San fransisco, US'), ('Cape Town, SA', 'Cape Town, SA')], max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(choices=[('Nairobi, Kenya', 'Nairobi, Kenya'), ('California, US', 'California, US'), ('London, UK', 'London, UK'), ('San fransisco, US', 'San fransisco, US'), ('Cape Town, SA', 'Cape Town, SA')], max_length=100),
        ),
        migrations.CreateModel(
            name='ShortList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('summary', models.CharField(max_length=1000)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shortlisted_jobs', to='HumanResource.applicant')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shortlist', to='HumanResource.job')),
            ],
        ),
    ]
