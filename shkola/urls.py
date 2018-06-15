"""shkola URL Configuration."""

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from blog.views import PostList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('upload/', include('django_file_form.urls')),
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
