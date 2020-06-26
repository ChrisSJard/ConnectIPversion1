from django.urls import path
from . import views

app_name = "searchApi"
urlpatterns = [
    path('academic', views.searchapi_academic_view, name='searchApi_academic-page'),
    path('industrial', views.searchapi_industrial_view, name='searchApi_industrial-page'),
    path('marketplace', views.searchapi_marketplace_view, name='searchApi_marketplace-page'),
]
