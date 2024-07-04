# users/views.py
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    # profiles/views.py
from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer




# users/views.py

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.urls import reverse

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect(reverse('admin:index'))  # Redirect to admin page
                else:
                    return redirect('user_home')  # Redirect to user home page
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = LoginForm()
    return render(request, 'User_management/login.html', {'form': form})


# users/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def user_home(request):
    return render(request, 'User_management/user_home.html')
