from django.conf.urls import url
from . import views

app_name = 'oktansite'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login_page, name='login_page'),
    url(r'^administrasi/', views.administration, name='administrasi'),
    url(r'^member/', views.member, name='member'),
    url(r'^user/', views.user, name='user'),
]
