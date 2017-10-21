from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import *
from django.conf import settings
from django.core.exceptions import ValidationError

# Create your views here.

# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB - 104857600
# 250MB - 214958080
# 500MB - 429916160
MAX_UPLOAD_SIZE = 2 * 1024 * 1024

#file size Handler
def size_checker(file):
    if file:
        if file.size > MAX_UPLOAD_SIZE:
            return False
        else:
            return True
    else:
        return True


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

def admin_dashboard(request, success=None, deleted=None):
    template = 'oktan/admin-dashboard.html'
    if request.user.is_staff:
        list_peserta = Team.objects.all()
        list_news = News.objects.all()
        timeline = Timeline.objects.all()
        return render(request, template,{
            'list_peserta': list_peserta,
            'list_news': list_news,
            'timeline': timeline,
            'success': success,
            'deleted': deleted,
        })
    else:
        return redirect('oktansite:index')

def generate_payment_proof(instance):
    return "OKTAN-ITB-2017-PROVE-"+instance.team_name.upper()+"-"+str(instance.uuid)

def generate_code(request, id):
    template = 'oktan/view_peserta.html'
    if request.user.is_staff:
        peserta = Team.objects.get(id=id)
        peserta.proof_code = generate_payment_proof(peserta)
        peserta.save()
        return redirect('oktansite:view_peserta', id)
    else:
        return redirect('oktansite:index')

def delete_code(request, id):
    template = 'oktan/view_peserta.html'
    if request.user.is_staff:
        peserta = Team.objects.get(id=id)
        peserta.proof_code = ""
        peserta.save()
        return redirect('oktansite:view_peserta', id)
    else:
        return redirect('oktansite:index')

def delete_peserta(request, id):
    peserta = Team.objects.get(id=id)
    peserta.delete()
    return redirect('oktansite:admin_dashboard')

def view_peserta(request, id):
    template = 'oktan/view_peserta.html'
    if request.user.is_staff:
        account_peserta = Account.objects.get(team=id)
        peserta = Team.objects.get(pk=id)
        return render(request, template, {
            'peserta': peserta,
            'account_peserta': account_peserta,
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
            attachment = request.FILES['attachment']
            if size_checker(attachment):
                article.attachment = attachment
                return redirect('oktansite:admin_dashboard')
                article.save()
            else:
                return render(request, template,{
                    "msg" : "File Size too Big",
                })
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
            news.attachment = request.FILES['attachment']
            news.save()
            return redirect('oktansite:admin_dashboard')
        else:
            return render(request, template, {'news': news})
    else:
        return redirect('oktansite:index')

def delete_news(request, id):
    if request.user.is_staff:
        news = News.objects.get(pk=id)
        news.delete()
        return redirect('oktansite:admin_dashboard')
    else:
        return redirect('oktansite:index')

def add_sponsor(request):
    template = 'oktan/addsponsor.html'
    sponsor = Sponsor.objects.first()
    if request.user.is_staff:
        if request.method == "POST":
            if sponsor:
                sponsor.src = request.FILES['sponsor']
                sponsor.save()
            else:
                sponsor = Sponsor()
                sponsor.src = request.FILES['sponsor']
                sponsor.save()
            return redirect('oktansite:addsponsor')
        else:
            return render(request, template, {
                'sponsor': sponsor,
            })
    else:
        return redirect('oktansite:index')

def add_media(request):
    template = 'oktan/addmedia.html'
    media = MediaPartner.objects.first()
    if request.user.is_staff:
        if request.method == "POST":
            if media:
                media.src = request.FILES['media']
                media.save()
            else:
                media= MediaPartner()
                media.src = request.FILES['media']
                media.save()
            return redirect('oktansite:add_media')
        else:
            return render(request, template, {
                'media': media,
            })
    else:
        return redirect('oktansite:index')

def edit_about(request):
    template = 'oktan/editabout.html'
    if request.user.is_staff:
        about = About.objects.first()
        if request.method == "POST":
            if (about):
                about.text = request.POST['text']
                about.save()
            else:
                about = About()
                about.text = request.POST['text']
                about.save()
            return redirect('oktansite:editabout')
        else:
            return render(request, template, {
                'about': about
            })
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
            return redirect('oktansite:admin_dashboard')
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
            return redirect('oktansite:admin_dashboard')
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
        return redirect('oktansite:admin_dashboard')
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
    sponsor = Sponsor.objects.first()
    media_partner = MediaPartner.objects.first()
    template = 'oktan/index.html'
    return render(request, template, {
        'timeline': timeline,
        'sponsor': sponsor,
        'media_partner': media_partner
    })

def about(request):
    sponsor = Sponsor.objects.first()
    media_partner = MediaPartner.objects.first()
    about = About.objects.first()
    template = 'oktan/about.html'
    return render(request, template, {
        'sponsor': sponsor,
        'media_partner': media_partner,
        'about': about,
    })

def news(request):
    template = 'oktan/news.html'
    articles = []
    sponsor = Sponsor.objects.first()
    media_partner = MediaPartner.objects.first()
    news_list = News.objects.order_by("-pub_date")
    count = 0
    for news in news_list:
        articles.append(news)
        count += 1
        if count == 5:
            break
    return render(request, template, {
        'news': articles,
        'sponsor': sponsor,
        'media_partner': media_partner,
    })

def blog(request, id):
    template = 'oktan/post.html'
    sponsor = Sponsor.objects.first()
    media_partner = MediaPartner.objects.first()
    article = News.objects.get(pk = id)
    return render(request, template, {
        'article' : article,
        'sponsor': sponsor,
        'media_partner': media_partner,
    })

def post(request):
    template = 'oktan/post.html'
    return render(request, template)

def gallery(request):
    sponsor = Sponsor.objects.first()
    media_partner = MediaPartner.objects.first()
    template = 'oktan/gallery.html'
    return render(request, template, {
        'sponsor': sponsor,
        'media_partner': media_partner,
    })

def contact(request):
    sponsor = Sponsor.objects.first()
    media_partner = MediaPartner.objects.first()
    template = 'oktan/contact.html'
    return render(request, template,{
        'sponsor': sponsor,
        'media_partner': media_partner,
    })

def login_page(request):
    template = 'oktan/login.html'
    return render(request, template)

@login_required
def administration(request):
    print (settings.MEDIA_ROOT)
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
            RAYON_ENUM ={
                      'bali': 'Bali',
                      'banyuwangi': 'Banyuwangi - Banyuwangi, Jember, Bondowoso, Situ bondo',
                      'bandung': 'Bandung - Bandung Raya, Sumedang, Subang',
                      'bogor': 'Bogor - Bogor, Sukabumi, Cianjur',
                      'cirebon': 'Cirebon - Cirebon, Majalengka, Indramayu, Tegal, Kuningan',
                      'karawang': 'Karawang - Karawang, Bekasi, Purwakarta',
                      'jakarta': 'Jakarta - Jakarta Raya',
                      'lampung': 'Lampung',
                      'makassar': 'Makassar - Sulawesi dan Indonesia Timur',
                      'malang': 'Malang - Malang, Lumajang, Mojokerto',
                      'medan': 'Medan - Banda Aceh, Medan',
                      'padang': 'Padang - Padang, Jambi, Riau',
                      'palembang': 'Palembang - Palembang, Bangka, Bengkulu',
                      'samarinda': 'Samarinda - Kalimantan',
                      'semarang': 'Semarang - Semarang, Demak, Salatiga, Kudus, Jepara',
                      'serang': 'Serang - Serang, Pandeglang, Cilegon, Lebak, Merak',
                      'surakarta': 'Surakarta - Surakarta, Boyolali, Karanganyar, Wonogiri',
                      'surabaya': 'Surabaya - Surabaya, Gresik, Lamongan, Mojokerto',
                      'tangerang': 'Tangerang',
                      'tasikmalaya': 'Tasikmalaya - Tasikmalaya, Ciamis, Garut, Banjar',
                  }
            rayon = request.POST["rayon"]
            if rayon:
                obj.rayon = RAYON_ENUM[rayon]
            if 'payment_proof' in request.FILES:
                proof_of_payment = request.FILES['payment_proof']
            if size_checker(proof_of_payment):
                obj.proof_of_payment = proof_of_payment
                obj.save()
                message = "Data Modified!"
                return render(request, template, {
                    'message': message,
                    'team': obj
                })
            else:
                message = "File Size is too big!"
                return render(request, template, {
                    'message': message,
                    'team': team
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
        obj.student_id_line_1 = request.POST["student_id_line_1"]
        obj.student_name_2 = request.POST["student_name_2"]
        obj.student_id_number_2 = request.POST["student_id_number_2"]
        obj.student_phone_number_2 = request.POST["student_phone_number_2"]
        obj.student_id_line_2 = request.POST["student_id_line_2"]
        if 'student_card_image_1' in request.FILES:
            obj.student_card_image_1 = request.FILES['student_card_image_1']
        if 'student_card_image_2' in request.FILES:
            obj.student_card_image_2 = request.FILES['student_card_image_2']
        if (size_checker(obj.student_card_image_2) and size_checker(obj.student_card_image_1)):
            obj.save()
            message = "Data Modified!"
            return render(request, template, {
                'message': message,
                'team': obj
            })
        else:
            message = "File Size is too Big"
            return render(request, template, {
                'message': message,
                'team': team
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
