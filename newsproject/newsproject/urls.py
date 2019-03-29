"""newsproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include,path
from myapp import views

urlpatterns = [
#    path('myapp/',include('myapp.urls')),
    path('', views.homepage_view, name='homepage_view'),# this is home page of our web site

    path('admin/', admin.site.urls),
    path('movies/',views.movienews_view),#directly goes to movienews_view
    path('sports/',views.sportsnews_view),
    path('politics/',views.Politicsnews_view),

]
