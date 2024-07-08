from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from rest_framework import viewsets
from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer
from django.contrib import messages

# View sets for API endpoints
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Regular views
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser or user.role == 'admin':
                    messages.info(request, f"Logged in as {user.email} (Admin)")
                    return redirect('admin_home')
                else:
                    messages.info(request, f"Logged in as {user.email} (User)")
                    return redirect('user_home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'user_management/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'user_management/register.html', {'form': form})

@login_required
def user_home(request):
    return render(request, 'user_management/user_home.html')

@login_required
@user_passes_test(lambda u: u.is_superuser or u.role == 'admin')
def admin_home(request):
    return render(request, 'user_management/admin_home.html')

def landing_page_view(request):
    return render(request, 'User_management/landing_page.html')