from django.urls import path

from . import views


app_name = 'theteachers'


urlpatterns = [

            #  Blog urls
            path('', views.TeacherList.as_view(), name='list'),
            path('<slug:slug>', views.Page.as_view(), name='page'),
            path('create/', views.CreateTeacher.as_view(), name='create'),
            path(
                'update/list/', views.UpdateTeacherList.as_view(),
                name='update_list'),
            path(
                'update/<slug:slug>/',
                views.UpdateTeacher.as_view(),
                name='update'),
            path(
                'delete/<slug:slug>/',
                views.DeleteTeacher.as_view(),
                name='delete'),
            ]
