from django.shortcuts import render

# Create your views here.

def ui_homepage_view(request):
    return render(request, 'UI/homepage.html')


def ui_about_view(request):
    return render(request, 'UI/about.html')


def ui_contact_view(request):
    return render(request, 'UI/contact.html')


def ui_faq_view(request):
    return render(request, 'UI/faq.html')


def ui_services_view(request):
    return render(request, 'UI/services.html')

