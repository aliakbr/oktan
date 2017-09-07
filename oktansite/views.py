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

@login_required
def administration(request):
    template = 'oktan/administrasi.html'
    team = request.user.team
    if request.method == 'GET':
        return render(request, template, {
            'team': team
        })
    else:
        try:
            obj = Team.objects.get(pk=team.id)
            obj.school_name = request.POST["school_name"]
            obj.supervisor_name = request.POST["supervisor_name"]
            obj.team_name = request.POST["team_name"]
            obj.save()
            message = "Data Modified!"
            return render(request, template, {
                'message': message,
                'team': obj
            })
        except ValidationError as e:
            message = ';'.join(e.messages)
            return render(request, template, {
                'message': message,
                'team': team
            })
        return render(request, template)

@login_required
def user(request):
    template = 'oktan/user.html'
    if request.method == 'GET':
        team = request.user.team
        return render(request, template, {
            'team': team
        })
    else:
        return render(request, template)

@login_required
def member(request):
    template = 'oktan/member.html'
    if request.method == 'GET':
        team = request.user.team
        return render(request, template, {
            'team': team
        })
    else:
        return render(request, template)

def login(request):
    if request.user.is_authenticated:
        return redirect('oktansite:administrasi')
    template = 'oktan/login.html'
    if request.method == 'GET':
        return render(request, template)
    else:
        email = request.POST['email']
        password = request.POST['password']
        acc = authenticate(email=email, password=password)
        print (acc)
        if acc is not None:
            auth_login(request, acc)
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
            new_team = Team()
            new_team.school_name = school_name
            new_team.supervisor_name = supervisor
            new_team.team_name = team_name
            new_team.save()
            new_account = Account()
            new_account.email = email
            new_account.password = password
            new_account.team = new_team
            new_account.save()
            acc = authenticate(email=email, password=password)
            print (acc)
            if acc is not None:
                auth_login(request, acc)
                return redirect('oktansite:administrasi')
            else:
                return render(request, template)
        except ValidationError as e:
            message = ';'.join(e.messages)
            return render(request, template, {
                'error_message': message
            })
    return render(request, template)
