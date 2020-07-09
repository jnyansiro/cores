"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from projects.views import *
from django.conf import settings
from django.conf.urls import handler404, handler500
from django.conf.urls import url
from django.conf.urls.static import static


urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL},name='logout'),
    path("index", index, name="index"),
    path("", indexs, name='web'),
    path("", include("authentication.urls")),
    path("", include("data_analysis.urls")),
    path("admin/", admin.site.urls),
    path("", include("projects.urls")),
    path("login", login, name="login"),
    path('privacy-policy', privacyPolicy, name='privacy-policy'),
    path('terms-conditions', termsConditions, name='terms-conditions'),
    path("registration", registration, name="registration"),
    path("forgetpassword", forgetpassword, name="forgetpassword"),
    url(r'^reset-password/$', recovery, name="reset-password")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = pagenotfound
handler500 = servererror
