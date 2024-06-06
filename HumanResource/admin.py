from django.contrib import admin
from .models import Job, Applicant, ShortList

# Register your models here.


@admin.register(Job)
class JobModelAdmin(admin.ModelAdmin):
    list_display = [
        'job_title', 'is_active', 'department', 'salary', 'location', 'brief_posting_description',  'date_posted']


@admin.register(Applicant)
class ApplicantModelAdmin(admin.ModelAdmin):
    list_display = [
        'first_name', 'last_name', 'gender', 'email', 'country', 'job', 'cv'
    ]


@admin.register(ShortList)
class ApplicantModelAdmin(admin.ModelAdmin):
    list_display = [
        'applicant', 'job', 'score', 'summary'
    ]
