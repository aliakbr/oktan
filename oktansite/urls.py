from django.conf.urls import url
from . import views

app_name = 'oktansite'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^administrasi/', views.administration, name='administrasi'),
    url(r'^member/', views.member, name='member'),
    url(r'^user/', views.user, name='user'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^loginadmin/', views.login_admin, name="loginadmin"),
    url(r'^admin/addnews', views.add_news, name="addnews"),
    url(r'^admin/editabout', views.edit_about, name="editabout"),
    url(r'^admin/addsponsor', views.add_sponsor, name="addsponsor"),
    url(r'^admin/', views.admin_dashboard, name="admindashboard")
]
