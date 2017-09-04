from django.shortcuts import render
from django.template import loader

# Create your views here.
def index(request):
    template = 'oktan/index.html'
    return render(request, template)
