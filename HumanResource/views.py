from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.contrib import messages
from .models import Job
import datetime


# Create your views here.


def home(request):
    jobs = Job.objects.all()
    job_data = {}
    for j in jobs:
        lower_bound = j.salary * 0.9
        upper_bound = j.salary * 1.1
        posted = (datetime.datetime.today().date() - j.date_posted).days
        applicants = j.applicants.all().count()
        shortlisted = j.shortlist.all().count()

        job_data[j.id] = {
            'job': j,
            'lower_bound': f"{lower_bound:.2f}",
            'upper_bound': f"{upper_bound:.2f}",
            'posted': posted,
            'applicants': applicants,
            'shortlisted': shortlisted
        }

    return render(request, 'app/hr_dashboard.html', {'job_data': job_data, 'total_jobs': Job.objects.all().count()})


def shortlist(request):
    return render(request, 'app/shortlist.html')


class NewJob(View):
    def get(self, request):
        return render(request, 'app/new_job.html')

    def post(self, request):
        job_title = request.POST.get('jobTitle')
        department = request.POST.get('department')
        salary = request.POST.get('salary')
        location = request.POST.get('location')
        introduction = request.POST.get('introduction')
        description = request.POST.get('description')
        responsibilities = request.POST.get('responsibilities')
        qualifications = request.POST.get('qualifications')

        if job_title:
            if department:
                if salary != '' and int(salary) > 0:
                    if location:
                        if introduction:
                            if description:
                                if responsibilities:
                                    if qualifications:
                                        try:
                                            # Add new job
                                            new_job = Job.objects.create(job_title=job_title, department=department,
                                                                         salary=salary, location=location,
                                                                         introduction=introduction,
                                                                         brief_posting_description=description,
                                                                         responsibilities=responsibilities,
                                                                         qualifications=qualifications)
                                            new_job.save()
                                            messages.success(request, 'New Job Added Successfully')
                                            return redirect('human-resource')

                                        except Exception as error:
                                            messages.warning('There was an issue adding a new job posting')
                                    else:
                                        messages.warning(request, 'Enter Required Job Qualifications')
                                else:
                                    messages.warning(request, 'Enter job responsibilities')
                            else:
                                messages.warning(request, 'Enter brief job description')
                        else:
                            messages.warning(request, 'Enter Job Intro')
                    else:
                        messages.warning(request, 'Select a location')
                else:
                    messages.warning(request, 'Enter a valid salary')

            else:
                messages.warning(request, 'Select a department')
        else:
            messages.warning(request, 'Enter Job title')

        return render(request, 'app/new_job.html', locals())


class EditJob(View):
    def get(self, request, job_id):
        job = Job.objects.filter(id=job_id)[0]
        return render(request, 'app/edit_job.html', locals())

    def post(self, request, job_id):
        job = Job.objects.filter(id=job_id)[0]
        is_active = request.POST.get('recruiting')
        job_title = request.POST.get('jobTitle')
        department = request.POST.get('department')
        salary = request.POST.get('salary')
        location = request.POST.get('location')
        introduction = request.POST.get('introduction')
        description = request.POST.get('description')
        responsibilities = request.POST.get('responsibilities')
        qualifications = request.POST.get('qualifications')

        if job:
            if job_title:
                if department:
                    if salary != '' and int(salary) > 0:
                        if location:
                            if introduction:
                                if description:
                                    if responsibilities:
                                        if qualifications:
                                            try:
                                                # update job
                                                job.job_title = job_title
                                                job.department = department
                                                job.salary = salary
                                                job.location = location
                                                job.introduction = introduction
                                                job.brief_posting_description = description
                                                job.responsibilities = responsibilities
                                                job.qualifications = qualifications
                                                job.is_active = is_active
                                                job.save()
                                                messages.success(request, 'Job Updated Successfully')
                                                return redirect('human-resource')

                                            except Exception as error:
                                                messages.warning('There was an issue adding a new job posting')
                                        else:
                                            messages.warning(request, 'Enter Required Job Qualifications')
                                    else:
                                        messages.warning(request, 'Enter job responsibilities')
                                else:
                                    messages.warning(request, 'Enter brief job description')
                            else:
                                messages.warning(request, 'Enter Job Intro')
                        else:
                            messages.warning(request, 'Select a location')
                    else:
                        messages.warning(request, 'Enter a valid salary')

                else:
                    messages.warning(request, 'Select a department')
            else:
                messages.warning(request, 'Enter Job title')

        return render(request, 'app/edit_job.html', locals())


def careers(request):
    jobs = Job.objects.filter(is_active=True)
    return render(request, 'app/careers.html', locals())


def job_detail_page(request, job_id):
    try:
        job = Job.objects.filter(id=job_id)[0]
        return render(request, 'app/job_detail.html', locals())
    except Exception as e:
        print(e)
        return HttpResponse('Not Found')

    
class ApplyJob(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


