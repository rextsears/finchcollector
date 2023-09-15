"""
URL configuration for finchcollector project.

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
from django.contrib import admin
from django.urls import path
from main_app import views
from main_app.views import FinchCreateView, FinchUpdateView, FinchDeleteView, ToyCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.finch_list, name='finch_list'),
    path('finch/<int:finch_id>/', views.finch_detail, name='finch_detail'),
    path('finches/create/', FinchCreateView.as_view(), name='add_finch'),
    path('finches/<int:pk>/edit/', FinchUpdateView.as_view(), name='edit_finch'),
    path('finches/<int:pk>/delete/', FinchDeleteView.as_view(), name='delete_finch'),
    path('finches/', views.finch_list, name='finch_list'),
    path('finch/<int:finch_id>/add-feeding/', views.add_feeding, name='add_feeding'),
    path('toys/create/<int:finch_id>/', ToyCreateView.as_view(), name='toy_create'),
    path('finch/<int:finch_id>/add-toy/', views.add_toy, name='add_toy'),
]
