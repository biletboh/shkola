"""shkola URL Configuration."""

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from filebrowser.sites import site

from blog.views import PostList

urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('upload/', include('django_file_form.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
] + i18n_patterns(
        path('', PostList.as_view()),
        path('', include('information.urls')),
        path('blog/', include('blog.urls')),
        path('teachers/', include('theteachers.urls')),
    )


if settings.DEBUG:
    urlpatterns += static(
                        settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
