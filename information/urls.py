from django.urls import path


from . import views


app_name = 'information'


urlpatterns = [
    path('about/', views.About.as_view(), name='about'),
    path('contacts/', views.Contacts.as_view(), name='contacts'),
]
