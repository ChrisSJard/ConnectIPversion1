from django.urls import path
from . import views

app_name = 'UI'
urlpatterns = [
    path('', views.ui_homepage_view, name='ui_home-page'),
    path('about/', views.ui_about_view, name='ui_about-page'),
    path('contact/', views.ui_contact_view, name='ui_contact-page'),
    path('customers/', views.ui_faq_view, name='ui_FAQ-page'),
    path('services/', views.ui_services_view, name='ui_services-page'),
]