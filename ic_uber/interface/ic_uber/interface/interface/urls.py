"""interface URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
#from django.urls import include, path
#from juris import views


#urlpatterns = [
	#path('juris', include('juris.urls')),
    #path('admin/', admin.site.urls),

#]

from django.conf import settings
from django.conf.urls.static import static
import os
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.static import serve
from django.contrib.auth import views as auth_views
import django.contrib.auth.urls
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView


# Up two folders to serve "site" content
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'site')

urlpatterns = [
    path('', TemplateView.as_view(template_name='main.html'), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
    path('juris/', include('juris.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^site/(?P<path>.*)$', serve,
        {'document_root': SITE_ROOT, 'show_indexes': True},
        name='site_path'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)