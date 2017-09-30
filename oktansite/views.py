from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import *
from django.core.exceptions import ValidationError

# Create your views here.

# Admin View
def login_admin(request):
    template = 'oktan/login-admin.html'
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('oktansite:admin_dashboard')
    if request.method == 'GET':
        return render(request, template)
    else:
        email = request.POST['email']
        password = request.POST['password']
        acc = authenticate(email=email, password=password)
        if acc is not None and acc.is_staff:
            auth_login(request, acc)
            return redirect('oktansite:admin_dashboard')
        else:
            return render(request, template)

def admin_dashboard(request):
    template = 'oktan/admin-dashboard.html'
    if request.user.is_staff:
        list_peserta = Team.objects.all()
        list_news = News.objects.all()
        timeline = Timeline.objects.all()
        return render(request, template,{
            'list_peserta': list_peserta,
            'list_news': list_news,
            'timeline': timeline,
            })
    else:
        return redirect('oktansite:index')

def add_news(request):
    template = 'oktan/addnews.html'
    if request.user.is_staff:
        if request.method == "POST":
            title = request.POST['title']
            body = request.POST['body']
            article = News()
            article.title = title
            article.text = body
            article.save()
            return redirect('oktansite:news')
        else:
            return render(request, template)
    else:
        return redirect('oktansite:index')

def edit_news(request, id):
    template = 'oktan/edit_news.html'
    news = News.objects.get(pk=id)
    if request.user.is_staff:
        if request.method == "POST":
            news.title = request.POST['title']
            news.text = request.POST['body']
            news.save()
            return redirect('oktansite:news')
        else:
            return render(request, template, {'news': news})
    else:
        return redirect('oktansite:index')

def delete_news(request, id):
    if request.user.is_staff:
        news = News.objects.get(pk=id)
        news.delete()
        return redirect('oktansite:news')
    else:
        return redirect('oktansite:index')

def edit_about(request):
    template = 'oktan/editabout.html'
    if request.user.is_staff:
        if request.method == "POST":
            about = About.objects.get(pk=1)
            about.text = request.POST['text']
            about.save()
            return redirect('oktansite:index')
        else:
            return render(request, template)
    else:
        return redirect('oktansite:index')

def add_timeline(request):
    template = 'oktan/add_timeline.html'
    if request.user.is_staff:
        if request.method == "POST":
            timeline = Timeline()
            timeline.tanggal = request.POST['tanggal']
            timeline.text = request.POST['body']
            timeline.save()
            return redirect('oktansite:index')
        else:
            return render(request, template)
    else:
        return redirect('oktansite:index')

def edit_timeline(request, id):
    template = 'oktan/edit_timeline.html'
    timeline = Timeline.objects.get(pk=id)
    if request.user.is_staff:
        if request.method == "POST":
            timeline.tanggal = request.POST['tanggal']
            timeline.text = request.POST['body']
            timeline.save()
            return redirect('oktansite:index')
        else:
            return render(request, template, {
                'timeline': timeline,
            })
    else:
        return redirect('oktansite:index')

def delete_timeline(request, id):
    if request.user.is_staff:
        timeline = Timeline.objects.get(pk=id)
        timeline.delete()
        return redirect('oktansite:index')
    else:
        return redirect('oktansite:index')

def add_sponsor(request):
    template = 'oktan/addsponsor.html'
    if request.user.is_staff:
        return render(request, template)
    else:
        return redirect('oktansite:index')

def admin_logout(request):
    if request.user.is_staff:
        auth_logout(request)
        return redirect(reverse('oktansite:index'))
    else:
        return redirect('oktansite:index')

# Site View
def index(request):
    timeline = Timeline.objects.all()
    template = 'oktan/index.html'
    return render(request, template, {
        'timeline': timeline
    })

def about(request):
    template = 'oktan/about.html'
    return render(request, template)

def news(request):
    template = 'oktan/news.html'
    articles = []
    news_list = News.objects.order_by("-pub_date")
    count = 0
    for news in news_list:
        articles.append(news)
        count += 1
        if count == 5:
            break
    return render(request, template, {'news': articles})

def post(request):
    template = 'oktan/post.html'
    return render(request, template)

def gallery(request):
    template = 'oktan/gallery.html'
    return render(request, template)

def contact(request):
    template = 'oktan/contact.html'
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
            if 'payment_proof' in request.FILES:
                obj.proof_of_payment = request.FILES['payment_proof']
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
    return render(request, template)

@login_required
def member(request):
    template = 'oktan/member.html'
    team = request.user.team
    if request.method == 'GET':
        return render(request, template, {
            'team': team
        })
    else:
        obj = Team.objects.get(pk=team.id)
        obj.student_name_1 = request.POST["student_name_1"]
        obj.student_id_number_1 = request.POST["student_id_number_1"]
        obj.student_phone_number_1 = request.POST["student_phone_number_1"]
        if 'student_card_image_1' in request.FILES:
            obj.student_card_image_1 = request.FILES['student_card_image_1']
        obj.student_name_2 = request.POST["student_name_2"]
        obj.student_id_number_2 = request.POST["student_id_number_2"]
        obj.student_phone_number_2 = request.POST["student_phone_number_2"]
        if 'student_card_image_2' in request.FILES:
            obj.student_card_image_2 = request.FILES['student_card_image_2']
        obj.save()
        message = "Data Modified!"
        return render(request, template, {
            'message': message,
            'team': obj
        })

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
        if acc is not None:
            auth_login(request, acc)
            return redirect('oktansite:user')
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
