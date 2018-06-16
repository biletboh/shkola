from django.urls import path

from . import views


app_name = 'blog'


urlpatterns = [

            #  Blog urls
            path('', views.PostList.as_view(), name='list'),
            path('<slug:slug>', views.Page.as_view(), name='page'),
            path('post/create/', views.CreatePost.as_view(), name='create'),
            path(
                'update/list/', views.UpdatePostList.as_view(),
                name='update_list'),
            path(
                'post/update/<slug:slug>/',
                views.UpdatePost.as_view(),
                name='update'),
            path(
                'post/delete/<slug:slug>/',
                views.DeletePost.as_view(),
                name='delete'),
            ]
