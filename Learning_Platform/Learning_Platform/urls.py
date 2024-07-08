# Learning_Platform/urls.py
from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.views.generic.base import RedirectView
from User_management.views import landing_page_view

urlpatterns = [
    path('', landing_page_view, name='landing_page'),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view(
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context={'title': 'Log in', 'year': datetime.now().year}
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),

    # Include URLs for User Management app
    path('api/users/', include('User_management.urls')),
    path('api/profiles/', include('User_management.urls')),

    # Include URLs for other apps as needed
    path('api/qualifications/', include('Qualification_management.urls')),
    path('api/subjects/', include('Student_Management.urls')),
    path('api/subjectcontent/', include('Subject_content_management.urls')),
    path('api/lecturers/', include('Lecturer_management.urls')),
    path('api/students/', include('Student_Management.urls')),
    path('api/auditlogs/', include('Admin_dashboard.urls')),
    
    # Redirect root URL to admin page
    # Uncomment this line if you want to redirect the root URL to the admin page
    # path('', RedirectView.as_view(url='/admin/', permanent=False), name='index'),
    
    # Route root URL to user_management app URLs
    path('', include('User_management.urls')),
]
