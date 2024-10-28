"""
URL configuration for office_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import landing_page
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.start,name='start'),
    path('all_emp',views.all_emp,name='all_emp'),
    path('add_emp',views.add_emp,name='add_emp'),
    path('remove_emp',views.remove_emp,name='remove_emp'),
    path('remove_emp/<int:emp_id>/', views.remove_emp, name='remove_emp'),
    path('filter_emp', views.filter_emp, name='filter_emp'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('emp_profile/<int:emp_id>/', views.emp_profile, name='emp_profile'),
    path('export_emp/', views.export_emp, name='export_emp'),
    path('landing/', landing_page, name='landing_page'),


]