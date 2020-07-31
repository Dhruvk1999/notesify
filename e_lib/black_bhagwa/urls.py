"""black_bhagwa URL Configuration

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
from django.urls import re_path,path,include
from . import views

urlpatterns = [
    re_path('^admin/', admin.site.urls),
    re_path('^$',views.HomePage.as_view(),name='home'),
    path('accounts/',include('accounts.urls',namespace='accounts',)),
    path('accounts/',include('django.contrib.auth.urls')),
    re_path(r'^test',views.TestPage.as_view(),name='test'),
    re_path(r'^thanks',views.ThanksPage.as_view(),name='thanks'),
    re_path(r'^posts/',include('posts.urls',namespace='posts')),
    re_path(r'^groups/',include('groups.urls',namespace='groups')),
    re_path(r'^links/',views.LinksPage.as_view(),name='links'),
    re_path(r'^message/$',views.MessageBoard.as_view(),name='message'), 
    re_path(r'^textbooks/$',views.Textbooks.as_view(),name='textbooks'),

]   
