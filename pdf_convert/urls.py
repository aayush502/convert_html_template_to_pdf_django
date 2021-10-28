"""pdf_convert URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from os import name
from django.contrib import admin
from django.urls import path, re_path
from pdf.views import *
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path(r'^pdf/(?P<product>\w+)/$', GeneratePdf.as_view(), name="report-pdf"),
    path('pdf/', GeneratePdf.as_view(), name="pdf"),
    path('index/', TemplateView.as_view(), name="index"),
    path('home/', HomeView.as_view(), name="home"),
    path('download', DownloadView.as_view(), name = "download"),
    path('student', StudentView.as_view(), name = "student"),
    path('student/<int:id>', DetaiView.as_view(), name="detail"),
    path('insurance', InsuranceView.as_view(), name="insurance"),

]
if settings.DEBUG:
    urlpatterns= urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
    urlpatterns= urlpatterns + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)

