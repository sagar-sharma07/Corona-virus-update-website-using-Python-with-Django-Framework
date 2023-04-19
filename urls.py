"""covid URL Configuration

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
from django.contrib import admin
from django.urls import path
from myapp import views
from covid import settings

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage/',views.home,name='home'),
    path('aboutPage/',views.about,name='about'),
    path('preventionPage/',views.prevention,name='prevention'),
    path('doctorsPage/',views.doctors,name='doctors'),
    path('faqPage/',views.faq,name='faq'),
    path('blogPage/',views.blog,name='blog'),
    path('contactPage/',views.contact,name='contact'),
    path('loginPage/',views.login,name='login'),
    path('situationPage/',views.situation,name='situation'),
    path('advicePage/',views.advice,name='advice'),
    path('symptomsPage/',views.symptoms,name='symptoms'),
    path('donarsPage/',views.donars,name='donars'),
    path('fullblogPage/<int:blogid>',views.fullblog,name='fullblog'),
    path('registerPage/',views.register,name='register'),
    path('forgetpasswordPage/',views.forgetpassword,name='forgetpassword'),
    path('myprofilePage/',views.myprofile,name='myprofile'),
    path('logoutPage/',views.logout,name='logout'),
    path('changepasswordPage/',views.changepassword,name='changepassword'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)