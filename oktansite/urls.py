from django.conf.urls import url
from . import views

app_name = 'oktansite'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.login_page, name='login_page'),
    url(r'^$', views.administration, name='administrasi'),
    url(r'^$', views.member, name='member'),
    url(r'^$', views.user, name='user'),
]
