from django.contrib.auth import views as auth_views
from django.urls import path


from . import views


app_name = 'information'


urlpatterns = [
    path('about/', views.About.as_view(), name='about'),
    path('contacts/', views.Contacts.as_view(), name='contacts'),
    path('login/',
         auth_views.LoginView.as_view(template_name='information/login.html'),
         {'next': '/blog/update/list/'}, name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(
             template_name='information/logout.html'),
         {'next': '/about/'}, name='logout'),
]
