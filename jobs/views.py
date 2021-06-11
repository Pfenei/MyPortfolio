from django.shortcuts import render, get_object_or_404
from .models import Job, Technology, Study, Framework, Course

game_frameworks = ['Unity', 'Godot', 'GameMaker', 'Unreal Engine']
web_frameworks = ['ASP.NET', 'Django']


# Create your views here.
def home(request):
    technologies = Technology.objects
    studies = Study.objects.all().order_by('-startDate')
    frameworks = Framework.objects
    courses = Course.objects.all().order_by('-completionDate')
    gamejobs = Job.objects.filter(mainframework__in=game_frameworks).order_by('-date')
    webjobs = Job.objects.filter(mainframework__in=web_frameworks).order_by('-date')
    schoolprojects = Job.objects.filter(is_schoolproject=True).order_by('-date')
    return render(request, 'jobs/home.html',
                  {'technologies': technologies, 'studies': studies, 'frameworks': frameworks, 'courses': courses, 'gamejobs': gamejobs, 'webjobs': webjobs, 'schoolprojects': schoolprojects})


def projects(request):
    gamejobs = Job.objects.filter(mainframework__in=game_frameworks).order_by('-date')
    webjobs = Job.objects.filter(mainframework__in=web_frameworks).order_by('-date')
    schoolprojects = Job.objects.filter(is_schoolproject=True).order_by('-date')
    return render(request, 'jobs/projects.html',
                  {'gamejobs': gamejobs, 'webjobs': webjobs, 'schoolprojects': schoolprojects})


def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job': job_detail})


def contact(request):
    return render(request, 'jobs/contact.html')
