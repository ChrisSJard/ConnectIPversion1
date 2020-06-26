from django.shortcuts import render

# Create your views here.


def searchapi_academic_view(request):
    return render(request, 'Searchapi/academic.html')


def searchapi_industrial_view(request):
    return render(request, 'Searchapi/industrial.html')


def searchapi_marketplace_view(request):
    return render(request, 'Searchapi/marketplace.html')