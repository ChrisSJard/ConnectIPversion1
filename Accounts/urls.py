from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='Accounts/login.html'), name='account-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Accounts/logout.html'), name='account-logout'),
    path('register/', views.account_signup_view, name='account-register'),
    path('register/setup', views.account_setprofile_view, name='account-register-profile'),
    path('profile/', views.account_userprofile_view, name='account-userprofile'),
    path('formsession/', views.account_ipassessment_view, name='account-ipAssessment')
]

