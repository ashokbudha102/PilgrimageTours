"""Tours URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import include
from about.views import about_view
urlpatterns = [
    path('1/admin/', admin.site.urls),
    path('contact/',include('contact.urls')),
    path('payment/',include('epay.urls')),
    path('home/',include('Home.urls')),
    path('signup/',include('Signup.urls')),
    path('login/', include('Login.urls')),
    path('about/',about_view,name='about')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
