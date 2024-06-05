from django.contrib import admin
from .models import Job, Applicant

# Register your models here.


@admin.register(Job)
class JobModelAdmin(admin.ModelAdmin):
    list_display = [
        'job_title', 'is_active', 'department', 'salary', 'location', 'brief_posting_description',  'date_posted']

    readonly_fields = ['shortlist']


@admin.register(Applicant)
class ApplicantModelAdmin(admin.ModelAdmin):
    list_display = [
        'first_name', 'last_name', 'gender', 'email', 'country', 'job', 'cv', 'shortlisted_jobs'
    ]
