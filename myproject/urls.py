"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from members.views import member_list, add_member, delete_member, car_list, add_car, delete_car

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', member_list, name='home'),
    path('members/', member_list, name='member_list'),
    path('members/add/', add_member, name='add_member'),
    path('members/delete/<int:member_id>/', delete_member, name='delete_member'),
    path('cars/', car_list, name='car_list'),
    path('cars/add/', add_car, name='add_car'),
    path('cars/delete/<int:car_id>/', delete_car, name='delete_car'),
]
