"""
URL configuration for essentiel_templates project.

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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index ,name='index'),
    path('use_static/' ,views.view_static,name='view_static') ,
    path('use_variables/' ,views.view_variables,name='view_variables'),
    path('use_attributs/' ,views.view_attributs,name='view_attributs'),
    path('use_alternatives/' ,views.view_alternatives,name='view_alternatives'),
    path('use_boucles/' ,views.view_boucle,name='view_boucles'),
    
]
