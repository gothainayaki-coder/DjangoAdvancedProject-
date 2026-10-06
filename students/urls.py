from django.urls import path
from . import views

urlpatterns = [
    path('', views.enrollment_create, name='enrollment_create'),
    path('success/', views.enrollment_success, name='enrollment_success'),
]