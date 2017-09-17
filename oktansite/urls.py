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
    url(r'^admin/', views.login_admin, name="login_admin"),
    url(r'^admin_dashboard/', views.admin_dashboard, name="admin_dashboard"),
    url(r'^admin_logout/', views.admin_logout, name="admin_logout")
]
