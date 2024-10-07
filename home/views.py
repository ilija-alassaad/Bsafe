

# Create your views here.
from django.shortcuts import render
from .models import Page
from blog.models import BlogPost
from django.http import Http404
from django.views import View


def home(request):
    pages = Page.objects.all()
    all_posts = BlogPost.objects.all().order_by('-date')
    return render(request, f'home/index.html', {'pages': pages, 'all_posts': all_posts})


def about(request):
    pages = Page.objects.all()
    return render(request, f'home/about.html', {'pages': pages})


def clients(request):
    pages = Page.objects.all()
    return render(request, f'home/clients.html', {'pages': pages})


def services(request):
    pages = Page.objects.all()
    return render(request, f'home/services.html', {'pages': pages})


def faq(request):
    pages = Page.objects.all()
    return render(request, f'home/faq.html', {'pages': pages})


class ServicesDetails(View):
    def get(self, request, service_type):
        service_template = {
            'HSEQ_management': 'HSEQ_management.html',
            'HSE_deployment': 'HSE_deployment.html',
            'HSE_Field_Trainings': 'HSE_Field_Trainings.html',
            'construction_management': 'construction_management.html',
            'website_applications': 'website_applications.html',
            'Marketing_Branding': 'Marketing_Branding.html',
            'Thesis_Guidance': 'thesis_guidance.html',
            'Import_Export': 'import_export.html',
        }
        template = service_template.get(service_type)

        if template is None:
            raise Http404("service not found")

        return render(request, f'home/{template}')
