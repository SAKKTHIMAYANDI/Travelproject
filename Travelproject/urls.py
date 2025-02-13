"""
URL configuration for Travelproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from TravelDetails.views.Registiondatas import Registiondatas
urlpatterns = [
    
    path('admin/travel-requests/<int:id>/<str:status>/', Registiondatas.update_travel_status, name='update_travel_status'),
    path('admin/view-details/<int:id>',Registiondatas.view_userdetails,name="view_userdetails"),
    path("admin/all_taskview/",Registiondatas.all_taskview,name="all_taskview"),
    path('admin/', admin.site.urls),
    path("",Registiondatas.home,name="home"),
    
    path("login/",Registiondatas.login_page,name="login_page"),
    path("Registion/",Registiondatas.Registion,name="Registion"),
    # travel_form 
    path('logout/', Registiondatas.user_logout, name='logout'),

    path("travel_form/",Registiondatas.travel_form,name="travel_form"),
    # travel_requests
    path("travel_requests/",Registiondatas.travel_requests,name="travel_requests"),
    
    
    
]
