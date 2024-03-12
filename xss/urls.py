from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('simple', views.xss_attack,name='xss'),
]