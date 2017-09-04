from django.shortcuts import render

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
