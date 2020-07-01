from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Accounts.models import DBPatent
from .forms import UserRegisterForm, ProfileInfoForm, PatentSummaryForm, ProfileImageForm


def account_login_view(request):
    return render(request, 'Accounts/login.html')


def account_logout_view(request):
    return render(request, 'Accounts/login.html')


def account_signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print (request.POST)
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
    patent1 = DBPatent.objects.get(id=1)
    patent2 = DBPatent.objects.get(id=2)
    patent3 = DBPatent.objects.get(id=3)
    context = {
        'pat1': patent1,
        'pat2': patent2,
        'pat3': patent3,
    }
    if request.method == "POST":
        obj = request.POST
        if obj.get("patent_id") == patent1.publicationNumber:
            patent1.creator = obj.get("user_id")
            patent1.stageSelected = True
            patent1.save()
            return redirect('account:account-ipAssessment')
        elif obj.get("patent_id") == patent2.publicationNumber:
            patent2.creator = obj.get("user_id")
            patent2.stageSelected = True
            patent2.save()
            return redirect('account:account-ipAssessment')
        elif obj.get("patent_id") == patent3.publicationNumber:
            patent3.creator = obj.get("user_id")
            patent3.stageSelected = True
            patent3.save()
            return redirect('account:account-ipAssessment')
        else:
            messages.error(request, f'Patent has already been assigned!')
    return render(request, 'Accounts/userprofile.html', context)


@login_required()
def account_ipassessment_view(request):
    if request.method == 'POST':
        form = PatentSummaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:account-userprofile')
    else:
        form = PatentSummaryForm()
    return render(request, 'Accounts/ipAssessment.html', {'form': form})


