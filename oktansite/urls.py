from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'oktansite'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name="about"),
    url(r'^news/', views.news, name="news"),
    url(r'^blog/(?P<id>\d+)/', views.blog, name="blog"),
    url(r'^post/', views.post, name="post"),
    url(r'^gallery/', views.gallery, name="gallery"),
    url(r'^contact/', views.contact, name="contact"),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^administrasi/', views.administration, name='administrasi'),
    url(r'^member/', views.member, name='member'),
    url(r'^user/', views.user, name='user'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^admin/', views.login_admin, name="login_admin"),
    url(r'^admin_dashboard/view_peserta/(?P<id>\d+)/', views.view_peserta, name="view_peserta"),
    url(r'^admin_dashboard/generate_code/(?P<id>\d+)/', views.generate_code, name="generate_code"),
    url(r'^admin_dashboard/delete_code/(?P<id>\d+)/', views.delete_code, name="delete_code"),
    url(r'^admin_dashboard/delete_peserta/(?P<id>\d+)/', views.delete_peserta, name="delete_peserta"),
    url(r'^admin_dashboard/add_media', views.add_media, name="add_media"),
    url(r'^admin_dashboard/add_timeline', views.add_timeline, name="add_timeline"),
    url(r'^admin_dashboard/edit_timeline/(?P<id>\d+)/', views.edit_timeline, name="edit_timeline"),
    url(r'^admin_dashboard/delete_timeline/(?P<id>\d+)/', views.delete_timeline, name="delete_timeline"),
    url(r'^admin_dashboard/add_news', views.add_news, name="addnews"),
    url(r'^admin_dashboard/edit_news/(?P<id>\d+)/', views.edit_news, name="edit_news"),
    url(r'^admin_dashboard/delete_news/(?P<id>\d+)/', views.delete_news, name="delete_news"),
    url(r'^admin_dashboard/editabout', views.edit_about, name="editabout"),
    url(r'^admin_dashboard/addsponsor', views.add_sponsor, name="addsponsor"),
    url(r'^admin_dashboard/', views.admin_dashboard, name="admin_dashboard"),
    url(r'^admin_logout/', views.admin_logout, name="admin_logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
