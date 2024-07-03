"""
Definition of urls for Learning_Platform.
"""

# Learning_Platform/urls.py
from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.views.generic.base import RedirectView

urlpatterns = [
    #path('', RedirectView.as_view(url='/admin/', permanent=False), name='index'),  # Redirect root URL to admin page
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view(
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context={'title': 'Log in', 'year': datetime.now().year, }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),
    path('api/users/', include('User_management.urls')),
    path('api/profiles/', include('User_management.urls')),
    path('api/qualifications/', include('Qualification_management.urls')),
    path('api/subjects/', include('Student_Management.urls')),
    path('api/subjectcontent/', include('Subject_content_management.urls')),
    path('api/lecturers/', include('Lecturer_management.urls')),
    path('api/students/', include('Student_Management.urls')),
    path('api/auditlogs/', include('Admin_dashboard.urls')),
   
]


