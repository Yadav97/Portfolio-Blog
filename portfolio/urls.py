"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

#we imort the core settings means settings of portfolio project
from django.conf import settings

from django.conf.urls.static import static

import jobs.views


urlpatterns = [
    path('admin/', admin.site.urls),
#jobs.views.home are our home page thats why we cannot include by include(jobs.urls) because jab user website par pahunchega toh hum direst 
#usko home.html dikhayenge and home .html jobs waala hoga.
#but in blog jab user blog waale link par click karega tab hum request portfolio ke urls.py se blog ki urls.py ko send karenge 
#and then blog/urls.py se html page kholnege (blog.views.functionname())so taht why we include the blog.urls

        path('', jobs.views.home, name="home"),
        path('blog/',include('blog.urls'))

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
