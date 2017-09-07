from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import *
from django.core.exceptions import ValidationError

# Create your views here.
def index(request):
    template = 'oktan/index.html'
    return render(request, template)

def login_page(request):
    template = 'oktan/login.html'
    return render(request, template)

def administration(request):
    template = 'oktan/administrasi.html'
    return render(request, template)

def user(request):
    template = 'oktan/user.html'
    return render(request, template)

def member(request):
    template = 'oktan/member.html'
    return render(request, template)

def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('oktansite:administrasi'))
    template = 'oktan/login.html'
    if request.method == 'GET':
        return render(request, template)
    else:
        email = request.POST['email']
        password = request.POST['password']
        team = authenticate(email=email, password=password)
        print (team)
        if team is not None:
            auth_login(request, team)
            return redirect('oktansite:administrasi')
        else:
            return render(request, template)

@login_required
def logout(request):
    auth_logout(request)
    return redirect(reverse('oktansite:index'))

def register(request):
    template = 'oktan/login.html'
    if request.method == 'POST':
        email= request.POST['email']
        password = request.POST['password']
        team_name = request.POST['team_name']
        supervisor= request.POST['supervisor']
        school_name = request.POST['school_name']

        # Register account
        try:
            new_account = Account()
            new_account.email = email
            new_account.password = password
            new_account.save()
            new_team = Team()
            new_team.account = new_account
            new_team.school_name = school_name
            new_team.supervisor = supervisor
            new_team.team_name = team_name
            new_team.save()
            team = authenticate(email=email, password=password)
            print (team)
            if team is not None:
                auth_login(request, team)
                return redirect('oktansite:administrasi')
            else:
                return render(request, template)
        except ValidationError as e:
            message = ';'.join(e.messages)
            return render(request, template, {
                'error_message': message
            })
    return render(request, template)
