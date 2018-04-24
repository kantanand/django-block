"""djblock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from pages.views import HomePageView

urlpatterns = [
    # This Urls should be present in top
    url(r'^$', HomePageView.as_view(), name='homepage'),
    url(r'^api/polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    # Important: you should add urls only on top not below this
    url(r'^(?P<path>.*)$', HomePageView.as_view(), name='homepage_redirect'),
]

if settings.DEBUG:  # Serve media files
    urlpatterns.insert(
        -1, 
        static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)[0]
    )
