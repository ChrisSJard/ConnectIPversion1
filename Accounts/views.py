from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileInfoForm, PatentSummaryForm


def account_login_view(request):
    return render(request, 'Accounts/login.html')


def account_logout_view(request):
    return render(request, 'Accounts/login.html')


def account_signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}!')
            return redirect('account:account-register-profile')
    else:
        form = UserRegisterForm()
    return render(request, 'Accounts/signup.html', {'form': form})


@login_required()
def account_setprofile_view(request):
    if request.method == 'POST':
        u_form = ProfileInfoForm(request.POST, instance=request.user.profile)
        i_form = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        if i_form.is_valid() and u_form.is_valid():
            i_form.save()
            u_form.save()
            return redirect('account:account-userprofile')
    else:
        u_form = ProfileInfoForm(instance=request.user.profile)
        i_form = ProfileImageForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'i_form': i_form,
    }
    return render(request, 'Accounts/setprofile.html', context)


@login_required()
def account_userprofile_view(request):
    return render(request, 'Accounts/userprofile.html')

@login_required()
def account_ipassessment_view(request):
    form = PatentSummaryForm()
    return render(request, 'Accounts/ipAssessment.html', {'form': form})


