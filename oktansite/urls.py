from django.conf.urls import url
from . import views

app_name = 'oktansite'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name="about"),
    url(r'^news/', views.news, name="news"),
    url(r'^gallery/', views.gallery, name="gallery"),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^administrasi/', views.administration, name='administrasi'),
    url(r'^member/', views.member, name='member'),
    url(r'^user/', views.user, name='user'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^admin/', views.login_admin, name="login_admin"),
    url(r'^admin_dashboard/addnews', views.add_news, name="addnews"),
    url(r'^admin_dashboard/editabout', views.edit_about, name="editabout"),
    url(r'^admin_dashboard/addsponsor', views.add_sponsor, name="addsponsor"),
    url(r'^admin_dashboard/', views.admin_dashboard, name="admin_dashboard"),
    url(r'^admin_logout/', views.admin_logout, name="admin_logout"),
    url(r'^editnews/(?P<id>\d+)/', views.edit_news, name="edit_news"),
    url(r'^deletenews/(?P<id>\d+)/', views.delete_news, name="delete_news")
]
